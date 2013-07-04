---
layout: post
title:  "Encoding Specifiers and Magical Mode Lines"
date:   2013-07-04 06:00:00
duration: "9"
categories: python vim
---


<!-- Encoding Specifiers and Magical Mode Lines -->
<iframe src="http://player.vimeo.com/video/69685215?title=0&amp;byline=0&amp;portrait=0&amp;color=4a8ac2" width="500" height="370" frameborder="0"> </iframe> 

## Ways Python infers encoding
1. Default Encodings
    - Python 2.7.x: 7-bit ASCII
    - Python 3.x: UTF-8
2. Magic Line
3. Using a BOM


## The Specifier should
- match the regular expression `coding[:=]\s*([-\w.]+)"`
- use encodings [supported by python](http://docs.python.org/3.3/library/codecs.html#standard-encodings)
- not have any other statement in the same line
- be listed in the first two lines


## Pattern 

    coding=<encoding>
    # coding=utf-8

The regular expression:

    coding[:=]\s*([-\w.]+)"

Vim style modelines:

    vim: set fileencoding=<encoding>:
    # vim: set fileencoding=utf-8:

Emacs style "modelines"

    -*- coding: <encoding> -*-
    # -*- coding: latin-1 -*-

## Templates in Vim
Initialise known file formats with a starter templates

    if has("autocmd")
        autocmd BufNewFile * silent! 0r ~/.vim/templates/template.%:e
    endif

Examples starter template for a python script

    #!/usr/bin/env python
    # vim: set fileencoding=utf-8:
    
    def main():
        pass

    if __name__ == '__main__':
        main()




## Excerpt from the [Pragmatic Unicode Talk](http://nedbatchelder.com/text/unipain.html)

- You cannot infer the encoding of *bytes*.
- Declared Encodings might be wrong.


## Relevant Documentation
### Python 
- [Python UNICODE howto](http://docs.python.org/3/howto/unicode.html)
- [2.7 Lexical analysis - 7-bit ASCII](http://docs.python.org/2.7/reference/lexical_analysis.html#lexical-analysis)
- [3.3 Lexical analysis - UTF-8](http://docs.python.org/3.3/reference/lexical_analysis.html#lexical-analysis)
- [3.3 - Standard Encodings](http://docs.python.org/3.3/library/codecs.html#standard-encodings)
- [3.3 Encoding declarations](http://docs.python.org/3.3/reference/lexical_analysis.html#encoding-declarations)
- [Text Vs. Data Instead Of Unicode Vs. 8-bit](http://docs.python.org/release/3.0.1/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit)

### PEPs
- [0263 - Defining Python Source Code Encodings](http://www.python.org/dev/peps/pep-0263/)
- [3120 - Using UTF-8 as the default source encoding](http://www.python.org/dev/peps/pep-3120/#specification)
- [3131 - Supporting Non-ASCII Identifiers](http://www.python.org/dev/peps/pep-3131/)

### Vim
- `:help bomb` - Enabling BOMs
- `:help modeline` Modelines
- `:help modelines` - Number of lines to check for a modeline
- `:help 'modeline'` - Toggle modeline recognition in vim


## Further Reading
- [BOM](https://en.wikipedia.org/wiki/Byte_order_mark)
- [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
- [BOM & UTF-8](http://en.wikipedia.org/wiki/UTF-8#Byte_order_mark)
- [7-bit ASCII](http://en.wikipedia.org/wiki/ASCII#7-bit)
- [Modeline Magic](http://vim.wikia.com/wiki/Modeline_magic)
- [Pragmatic Unicode](http://nedbatchelder.com/text/unipain.html)
- [The Updated Guide to Unicode on Python](http://lucumr.pocoo.org/2013/7/2/the-updated-guide-to-unicode/)
- [Unicode in Python, Completely Demistified](http://farmdev.com/talks/unicode/)
- [Getting Unicode right in Python - Nick's Blog](http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python)
- [Sublime Text Modelines plugin does not confirm to the required regex](https://github.com/SublimeText/Modelines)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets - No Excuses!](http://www.joelonsoftware.com/articles/Unicode.html)
