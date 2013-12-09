#!/usr/bin/env python

import re

def plain(text):
    ansi_escape = re.compile(r'\x1b[^m]*m')
    return ansi_escape.sub('', text)

def _wrap_with(code):
    def inner(text, bold=False):
        c = code
        if bold:
            c = "1;%s" % c
        return "\033[%sm%s\033[0m" % (c, text)
    return inner

fred = _wrap_with('31')
fgreen = _wrap_with('32')
fyellow = _wrap_with('33')
fblue = _wrap_with('34')
fmagenta = _wrap_with('35')
fcyan = _wrap_with('36')
fwhite = _wrap_with('37')

bred = _wrap_with('41')
bgreen = _wrap_with('42')
byellow = _wrap_with('43')
bblue = _wrap_with('44')
bmagenta = _wrap_with('45')
bcyan = _wrap_with('46')
bwhite = _wrap_with('47')
