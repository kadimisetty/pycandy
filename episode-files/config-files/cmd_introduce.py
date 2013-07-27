#!/usr/bin/env python3
# vim: set fileencoding=utf-8 nonumber:
#
# Example:
# $ ./cmd_introduce.py -- name=Bender
#                      -- mail=bender@ilovebender.com
#                      -- http=ilovebender.com


import sys

user = {}
for v in sys.argv:
    if v[2:6] == 'name': user[ v[2:6] ] = v[7:]
    if v[2:6] == 'mail': user[ v[2:6] ] = v[7:]
    if v[2:6] == 'http': user[ v[2:6] ] = v[7:]

print('USER DETAILS')
for v in user:
    print('{} - {}'.format(v.upper(), user[v]))
