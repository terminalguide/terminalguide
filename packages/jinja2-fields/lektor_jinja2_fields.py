# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from lektor.types.formats import MarkdownType
from lektor.types.primitives import StringType, StringsType, TextType, HtmlType
from lektor.context import get_ctx
from lektor.markdown import Markdown

# StringType, StringType, TextType, HtmlType, MarkdownType

def apply_jinja2(s):
    ctx = get_ctx()
    env = ctx.env

    context = {}
    return env.jinja_env.from_string(s).render(context)

class Jinja2WrapperDescriptor(object):

    def __init__(self, raw, wrapped):
        self.raw = raw
        self.wrapped = wrapped
        self.is_cached = False
        self.cached = None

    def __get__(self, obj, type=None):
        if obj is None:
            return self

        if not self.is_cached:
            self.raw.value = apply_jinja2(self.raw.value)
            self.cached = self.wrapped(self.raw)
            self.is_cached = True

        return self.cached

class StringWithJinja2Type(StringType):
    name = 'string+jinja2'

    def value_from_raw(self, raw):
        return Jinja2WrapperDescriptor(raw, super().value_from_raw)


class StringsWithJinja2Type(StringsType):
    name = 'strings+jinja2'

    def value_from_raw(self, raw):
        return Jinja2WrapperDescriptor(raw, super().value_from_raw)


class TextWithJinja2Type(TextType):
    name = 'text+jinja2'

    def value_from_raw(self, raw):
        return Jinja2WrapperDescriptor(raw, super().value_from_raw)

class HtmlWithJinja2Type(HtmlType):
    name = 'html+jinja2'

    def value_from_raw(self, raw):
        return Jinja2WrapperDescriptor(raw, super().value_from_raw)



class Jinja2MarkupDescriptor(object):

    def __init__(self, source):
        self.source = source

    def __get__(self, obj, type=None):
        if obj is None:
            return self

        return Markdown(apply_jinja2(self.source), record=obj)


class MarkdownWithJinja2Type(MarkdownType):
    name = 'markdown+jinja2'

    def value_from_raw(self, raw):
        return Jinja2MarkupDescriptor(raw.value or u'')


class Jinja2FieldsPlugin(Plugin):
    name = 'jinja2-fields'
    description = u'Add markdown and string field with Jinja2 preprocessing.'

    def on_setup_env(self, **extra):
        self.env.add_type(MarkdownWithJinja2Type)
        self.env.add_type(StringWithJinja2Type)
        self.env.add_type(StringsWithJinja2Type)
        self.env.add_type(TextWithJinja2Type)
        self.env.add_type(HtmlWithJinja2Type)
