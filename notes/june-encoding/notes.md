vim: set filetype=markdown:
# File Encodings

[PEP 0263](http://www.python.org/dev/peps/pep-0263/)

Describe as a "magic line" in the first two lines-

    coding=<encoding name>
    coding[:=]\s*([-\w.]+)"

    example:
    #coding=utf-8

    Combine it with editor modelines for lines such as-
    For Emacs-

    #!/usr/bin/python
    # -*- coding: <encoding name> -*-

    or for vim-

    #!/usr/bin/python
    # vim: set fileencoding=<encoding name> :
    # vim: set fileencoding=utf-8:

    Not 

    #set fileenc=


If the encoding is unknown to Python, an error is
raised during compilation. There must not be any
Python statement on the line that contains the
encoding declaration.

## Examples


Without encoding comment, Python's parser will
assume ASCII text:


    #!/usr/bin/python
    # -*- coding: latin-1 -*-
    import os, sys
    ...


    #!/usr/local/bin/python
    import os, sys

[Working with Unicode](http://vim.wikia.com/wiki/Working_with_Unicode)
Gotta have this within your vim setting-

    if has("multi_byte")
      if &termencoding == ""
        let &termencoding = &encoding
      endif
      set encoding=utf-8
      setglobal fileencoding=utf-8
      "setglobal bomb
      set fileencodings=ucs-bom,utf-8,latin1
    endif

Do not use 
    set enc=utf-8

When set with the encoding as 'bomb' (boolean)
vim will put a "byte order mark" (or BOM for
short) at the start of Unicode files. This option
is irrelevant for non-Unicode files (iso-8859,
etc.). This BOM is the codepoint U+FEFF, which is
represented on disk as follows:

UTF-8: EF BB BF
UTF-16be: FE FF
UTF-16le: FF FE
UTF-32be: 00 00 FE FF
UTF-32le: FF FE 00 00


## What is Unicode 

A text string is simply a series of these codepoints, representing the character for each element in the string.





## Notes


## TODO
What is `unicode_literals` (like for 2.6/2.7)
    from __future__ import unicode_literals


## Further Information
- [http://farmdev.com/talks/unicode/](Unicode in Python, Completely Demistified)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets - No Excuses!](http://www.joelonsoftware.com/articles/Unicode.html)
- [Getting Unicode right in Python - Nick's Blog](http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python)
- [Text Vs. Data Instead Of Unicode Vs. 8-bit¶](http://docs.python.org/release/3.0.1/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit)
