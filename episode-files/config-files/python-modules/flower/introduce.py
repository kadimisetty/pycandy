#!/usr/bin/env python3
# vim: set fileencoding=utf-8 nonumber:


from information import user

print('USER DETAILS')
for k in user:
    print('{} - {}'.format(k.upper(), user[k]))
