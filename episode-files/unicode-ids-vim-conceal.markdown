
## Topics 
- Vim's conceal
- Python Identifiers written with Unicode Literals

These Identifiers can be 
1. Python 2 - Only a-z, A-Z, digits, underscore. Lexical Analysis:
    identifier ::=  (letter|"_") (letter | digit | "_")*
    letter     ::=  lowercase | uppercase
    lowercase  ::=  "a"..."z"
    uppercase  ::=  "A"..."Z"
    digit      ::=  "0"..."9"

2. Python 3 - Cetain Unicode Letter Categories 
    identifier   ::=  xid_start xid_continue*
    id_start     ::=  <all characters in general categories Lu, Ll, Lt, Lm, Lo, Nl, the underscore, and characters with the Other_ID_Start property>
    id_continue  ::=  <all characters in id_start, plus characters in the categories Mn, Mc, Nd, Pc and others with the Other_ID_Continue property>
    xid_start    ::=  <all characters in id_start whose NFKC normalization is in "id_start xid_continue*">
    xid_continue ::=  <all characters in id_continue whose NFKC normalization is in "id_continue*">

## Example
Variable
    नाम = 'Sri Kadimisetty'
    print(नाम)

Function
    def pi-character():
        return 3.14

## Understanding the Python 3 Identifiers Lexical Syntax
- Within the ASCII Range use unicode range (U+0001..U+007F)
- Identfier syntax is `<XID_Start> <XID_Continue`
- `<XID_Start>` consists of:
    * Lu : Uppercase Letters
    * Ll : Lowercase Letters
    * Lt : Titlecase Letters
    * Lm : Modifier Letters
    * Lo : Other Letters
    * Nl : Letter Numbers
    * Underscore
    * and - 
        "and characters carrying the Other_ID_Start property. XID_Start then closes this set under normalization, by removing all characters whose NFKC normalization is not of the form ID_Start ID_Continue* anymore."
- `<XID_Continue>` consists of
    * Characters in `<XID_Start>`
    * Mn : Non spacing Marks
    * Mc : Spacing Combined Marks
    * Nd : Decimal Numbers
    * Pc : Connector Punctuations
    * and - 
        and characters carryig the Other_ID_Continue property. Again, XID_Continue closes this set under NFKC-normalization; it also adds U+00B7 to support Catalan.

## PEP 3131 Policy Specification Adherance
- Python Coding Style
- Standard Library Identifiers should only use ASCII identifiers and english words when possible
- String Literals and comments must be in ASCII, except in
    * test cases testing non-ASCII features
    * names of Authors etc. Non-Lating based Names must provies a latin transliteration of their names


## Notes
- For characters in ASCII range use ASCII range (U+0001..U+007F), same as Py 2.x
- For others use the version of Unicode Cahracter Database used by the `unicodeddata` module - [UCD 6.1.0](http://www.unicode.org/Public/6.1.0/ucd/)
### Unicode Normalization
- [Normalization](http://en.wikipedia.org/wiki/Unicode_equivalence#Normalization)
- All identifiers are converted into the normal form NFKC while parsing; comparison of identifiers is based on NFKC.
- What is normalizing identifiers? Types considered when implementing were:
    * NFC
    * NKFC

## Restrictions
### Keywords
    False      class      finally    is         return
    None       continue   for        lambda     try
    True       def        from       nonlocal   while
    and        del        global     not        with
    as         elif       if         or         yield
    assert     else       import     pass
    break      except     in         raise

### [Reserved Classes of Identifiers](http://docs.python.org/2/reference/simple_stmts.html#import)
`_*`
:Not imported in `from module import *`
- When not in interactive environment, it has no special meaning
- In interactive interpreter, it stores the result of last evaluation
- Refer to the [`builtins` module](http://docs.python.org/3/library/builtins.html#module-builtins)
    * [Builtin Constants](http://docs.python.org/3/library/constants.html#built-in-constants)
    * [Builtin Functions](http://docs.python.org/3/library/functions.html#built-in-functions)

`__*__`
: System Defined Names. Definited by Implementations and Interpreters

`__*`
: Class-Private Names

## Screencast Order
- Vim 
    * Features
    * Conceal
- Lexical Syntax & Identifiers
- Unicode names for ids
- Character Range
- Restrictions
- Normalization


## References
### Documetation
Python 3
- [Lexical Analysis - Identifiers and Keywords](http://docs.python.org/3/reference/lexical_analysis.html#identifiers)
- [unicodedata module](http://docs.python.org/3/library/unicodedata.html#module-unicodedata)
- [Reserved class of Identifiers](http://docs.python.org/3/reference/lexical_analysis.html#reserved-classes-of-identifiers)
- [Keywords](http://docs.python.org/3/reference/lexical_analysis.html#keywords)

Python 2
- [Lexical Analysis](http://docs.python.org/2/reference/lexical_analysis.html#identifiers)

PEP
- [PEP 3131 - Supporting Non-ASCII Identifiers](http://www.python.org/dev/peps/pep-3131/)

### Further Reading
- [Pros and Cons - Stack Exchange](http://programmers.stackexchange.com/questions/16010/is-it-bad-to-use-unicode-characters-in-variable-names)
- [Valid Identifiers in Non-Normative HTML](http://www.dcl.hpi.uni-potsdam.de/home/loewis/table-3131.html)
- [Cons of Unicode Identifiers](http://mail.python.org/pipermail/python-3000/2007-June/008161.html)
