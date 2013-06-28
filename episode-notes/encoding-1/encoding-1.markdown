# Encoding Specifiers


## Notes
Pattern `coding=<encoding name>`. 
Example     
    #coding=utf-8

The regular expression
    coding[:=]\s*([-\w.]+)"

Vim style modelines
    # vim: set fileencoding=utf-8:

Emacs style "modelines"
    # -*- coding: <encoding name> -*-
    # -*- coding: latin-1 -*-


## Requirements
* Encoding should be known to python
* Should not contain another statment
* Should be specified within the first two lines


## Relevant Documentation
### Python 
* [Python UNICODE howto](http://docs.python.org/3/howto/unicode.html)
* [Text Vs. Data Instead Of Unicode Vs. 8-bit](http://docs.python.org/release/3.0.1/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit)
* [3.3 - Standard Encodinga](http://docs.python.org/3.3/library/codecs.html#standard-encodings)
* [2.7 Lexical analysis - 7-bit ASCII](http://docs.python.org/2.7/reference/lexical_analysis.html#lexical-analysis)
* [3.3 Lexical analysis - UTF-8](http://docs.python.org/3.3/reference/lexical_analysis.html#lexical-analysis)
* [3.3 Encoding declarations](http://docs.python.org/3.3/reference/lexical_analysis.html#encoding-declarations)

### PEPs
* [0 - Index of Python Enhancement Proposals](http://www.python.org/dev/peps/)
* [263 - Defining Python Source Code Encodings](http://www.python.org/dev/peps/pep-0263/)
* [3120 - Using UTF-8 as the default source encoding](http://www.python.org/dev/peps/pep-3120/#specification)
* [3131 - Supporting Non-ASCII Identifiers](http://www.python.org/dev/peps/pep-3131/)

### Vim
* `:help bomb` - Enabling BOMs
* `:help modeline` Modelines
* `:help 'modeline'` - Toggle modeline recognition in vim
* `:help modelines` - Number of lines to check for a modeline


## Further Information
* [7-bit ASCII](http://en.wikipedia.org/wiki/ASCII#7-bit)
* [BOM & UTF-8](http://en.wikipedia.org/wiki/UTF-8#Byte_order_mark)
* [Modeline Magic](http://vim.wikia.com/wiki/Modeline_magic)
* [BOM](https://en.wikipedia.org/wiki/Byte_order_mark)
* [Getting Unicode right in Python - Nick's Blog](http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python)
* [Sublime Text Modelines plugin does not confirm to the required regex](https://github.com/SublimeText/Modelines)
* [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets - No Excuses!](http://www.joelonsoftware.com/articles/Unicode.html)
* [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
* [Unicode in Python, Completely Demistified](http://farmdev.com/talks/unicode/)
* [http://farmdev.com/talks/unicode/](Unicode in Python, Completely Demistified)
