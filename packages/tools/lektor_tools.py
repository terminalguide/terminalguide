# -*- coding: utf-8 -*-
import os.path

from lektor.pluginsystem import Plugin
from lektor.context import get_ctx

def snip_resolver(name):
    ctx = get_ctx()
    if not ctx:
        return 'DEVMODE?'
    val = 'SNIPPET ' + name
    env = ctx.env
    filename = os.path.join(env.root_path, 'snippets', name + '.txt')
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            val = f.read()
        ctx.record_dependency(filename)
    else:
        val = 'SNIPPET missing: ' + name
    return val

def mode_link(mode):
    try:
        ctx = get_ctx()
        if not ctx:
            return 'DEVMODE?'

        pad = ctx.pad

        record = pad.get('/mode/' + mode)
        if record:
            title = record['title']
            if title.endswith(')'):
                title = title[:title.rindex('(')]
            title = title.lower()
        else:
            title = "mode not found: " + mode
        return '<a href="{url}">{title}</a>'.format(title=title, url='/mode/' + mode)
    except Exception as ex:
        print('failed:', ex)
        raise


def seq_link(seq):
    try:
        ctx = get_ctx()
        if not ctx:
            return 'DEVMODE?'

        pad = ctx.pad

        record = pad.get('/seq/' + seq)
        if record:
            title = record['title']
            if title.endswith(')'):
                title = title[:title.rindex('(')]
            title = title.lower()
        else:
            title = "Sequence not found: " + seq
        return '<a href="{url}">{title}</a>'.format(title=title, url='/seq/' + seq)
    except Exception as ex:
        print('failed:', ex)
        raise


def sgr_link(seq):
    try:
        ctx = get_ctx()
        if not ctx:
            return 'DEVMODE?'

        pad = ctx.pad

        record = pad.get('/attr/' + seq)
        if record:
            title = record['title']
            if title.endswith(')'):
                title = title[:title.rindex('(')]
            title = title.lower()
        else:
            title = "Attribute not found: " + seq
        return '<a href="{url}">{title}</a>'.format(title=title, url='/attr/' + seq)
    except Exception as ex:
        print('failed:', ex)
        raise


def jinja_hex(s):
    r = []
    for ch in s:
        r.append(hex(ord(ch))[2:].rjust(2,'0'))
    return " ".join(r)

class ToolsPlugin(Plugin):
    name = 'tools'
    description = u'Internal tools.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['hex'] = jinja_hex
        self.env.jinja_env.globals['snip'] = snip_resolver
        self.env.jinja_env.globals['mode_link'] = mode_link
        self.env.jinja_env.globals['seq_link'] = seq_link
        self.env.jinja_env.globals['sgr_link'] = sgr_link
