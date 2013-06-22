#! /usr/bin/env python

# Say Hello in different languages

hello = {
    "halløj" : "danish",
    "hæ"     : "icelandic",
    "xin"    : "vietnamese",
    "¡hola"  : "spanish",
    "안녕"   : "korean",
    "Γεια"   : "greek",
    "नमस्ते"   : "hindi",
    "నమస్తే"   : "telugu",
    }

import getpass
username = getpass.getuser()

print(['{} {}'.format(k, username) for k in hello.keys()])
