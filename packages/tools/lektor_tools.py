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

def snipi_resolver(name):
    val = snip_resolver(name)
    return val.strip()

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

def seq_param(name):
    ret = "<span class='term-param'><ruby>Ⓝ"
    ret += "<rt>" + name + "&nbsp;</rt>"
    ret += "</ruby></span>"
    return ret

def seq(l):
    ret = "<span class='term-literal'><ruby>"
    for i in l:
        v = i
        if i == '\033':
            v = 'ESC'
        elif i == '\0':
            v = 'NUL'
        elif i == '\b':
            v = 'BS'
        elif i == '\n':
            v = 'LF'
        elif i == '\r':
            v = 'CR'
        elif i == '\177':
            v = 'DEL'
        ret += v + "<rt>" + hex(ord(i))[2:].rjust(2,'0') + "&nbsp;</rt>"
    ret += "</ruby></span>"
    return ret

def jinja_hex(s):
    r = []
    for ch in s:
        r.append(hex(ord(ch))[2:].rjust(2,'0'))
    return " ".join(r)

force_new_line = '<span style="display:block"></span>'

jinja_miss = force_new_line + 'ð '
jinja_info = force_new_line + 'ð '
class ToolsPlugin(Plugin):
    name = 'tools'
    description = u'Internal tools.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['hex'] = jinja_hex
        self.env.jinja_env.globals['seq'] = seq
        self.env.jinja_env.globals['seq_param'] = seq_param
        self.env.jinja_env.globals['snip'] = snip_resolver
        self.env.jinja_env.globals['snipi'] = snipi_resolver
        self.env.jinja_env.globals['mode_link'] = mode_link
        self.env.jinja_env.globals['seq_link'] = seq_link
        self.env.jinja_env.globals['sgr_link'] = sgr_link
        self.env.jinja_env.globals['info'] = jinja_info
        self.env.jinja_env.globals['miss'] = jinja_miss
