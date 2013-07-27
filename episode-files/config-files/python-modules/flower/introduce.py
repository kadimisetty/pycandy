#!/usr/bin/env python
# vim: set fileencoding=utf-8 nonumber:


from information import user

print('USER DETAILS')
for k in user:
    print('{} - {}'.format(k.upper(), user[k]))
