#! /usr/bin/env python
# vim: set fileencoding=utf-8:


hello = {
    "hæ"   : "icelandic",
    "Γεια" : "greek",
    "नमस्ते" : "hindi",
    "నమస్తే" : "telugu",
    "안녕" : "korean",
    }

import getpass
print(['{} {}'.format(k, getpass.getuser()) for k in hello.keys()])
