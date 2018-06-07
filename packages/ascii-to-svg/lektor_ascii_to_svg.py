# -*- coding: utf-8 -*-

import shlex
import hashlib
import base64
from subprocess import PIPE, Popen

from lektor.context import get_ctx
import lektor.context
from lektor.pluginsystem import Plugin
from lektor.types import Type

def calla2s(text, *args):
    p = Popen(
        ['a2s', *args],
        stdin=PIPE, stdout=PIPE, stderr=PIPE)

    out, err = p.communicate(text.encode())
    if p.returncode != 0:
        raise RuntimeError('a2s: "%s"' % err)

    return out.decode()

class SVG(object):
    def __init__(self, svg, doctype):
        self.svg = svg
        self.doctype = doctype

    def as_url(self):
        ctx = get_ctx()
        print(ctx.record)
        content = self.doctype + self.svg
        digest = base64.urlsafe_b64encode(hashlib.sha224(content.encode()).digest()).decode()
        digest = digest.rstrip('=')
        p = "{}/diagram-{}.svg".format(ctx.record.path, digest)
        @ctx.sub_artifact(p, sources=[ctx.record.source_filename],
                          config_hash=digest)
        def build_stylesheet(artifact):
            with artifact.open('w') as f:
                f.write(content)
        return p

    def width(self):
        start = self.svg.find('<svg ') + 4
        end = self.svg.find(' ', start + 1)
        s = self.svg[start:end]
        print(s)
        print(s.split('"')[1][:-2])
        return int(s.split('"')[1][:-2])

    def __html__(self):
        return self.svg

class AsciiToSvgType(Type):
    widget = 'multiline-text'

    def value_from_raw(self, raw):
        inval = raw.value or u''
        options = []
        if inval.startswith('!'):
            params = inval[1:inval.find('\n')]
            options += shlex.split(params)
            inval = inval[inval.find('\n')+1:]
        svg = calla2s(inval, *options)
        # skip first line, because that is the svg doctype we don't want here
        doctype = svg[:svg.find('\n')+1]
        svg = svg[svg.find('\n')+1:]
        record = None
        return SVG(svg, doctype)


class AsciiToSvgPlugin(Plugin):
    name = 'Ascii to SVG'
    description = u'Adds asciitosvg field type to Lektor.'

    def on_setup_env(self, **extra):
        self.env.add_type(AsciiToSvgType)
