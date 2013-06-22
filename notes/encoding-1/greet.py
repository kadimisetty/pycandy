#! /usr/bin/env python


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

# Greet user in different languages
import getpass
username = getpass.getuser()
print(['{} {}'.format(k, username) for k in hello.keys()])
