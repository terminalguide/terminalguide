# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin


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
