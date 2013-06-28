#! /usr/bin/env python


hello = {
    "hæ"   : "icelandic",
    "नमस्ते" : "hindi",
    "నమస్తే" : "telugu",
    "안녕" : "korean",
    }

import getpass
print(['{} {}'.format(k, getpass.getuser()) for k in hello.keys()])
