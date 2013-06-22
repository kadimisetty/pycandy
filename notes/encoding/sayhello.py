# Say Hello in different languages
#coding=utf-8

hello = {
    "halløj" : "danish",
    "hæ"     : "icelandic",
    "xin"    : "vietnamese",
    "¡"      : "spanish",
    "안녕"   : "korean",
    "Γεια"   : "greek",
    "नमस्ते"   : "hindi",
    "నమస్తే"   : "telugu",
    }

import getpass
username = getpass.getuser()

print(['{} {}'.format(k, username) for k in hello.keys()])
