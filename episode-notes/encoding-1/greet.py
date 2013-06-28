#! /usr/bin/env python
#coding=utf-8


hello = {
        'icelandic':  'hæ',
        'hindi':      'नमस्ते',
        'telugu':     'నమస్తే',
        'korean':     '안녕'
    }

import getpass
print(['{} {}'.format(k, getpass.getuser()) for k in hello.values()])

안녕
