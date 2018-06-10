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
