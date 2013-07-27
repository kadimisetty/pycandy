#!/usr/bin/env python3
# vim: set fileencoding=utf-8 nonumber:


import sys

user = {}
for v in sys.argv:
    if v[2:6] == 'name': user[ v[2:] ] = v[7:]
    if v[2:6] == 'mail': user[ v[2:] ] = v[7:]
    if v[2:6] == 'http': user[ v[2:] ] = v[7:]

print('USER DETAILS')
for k in user:
    print('{} - {}'.format(k.upper(), user[k]))
