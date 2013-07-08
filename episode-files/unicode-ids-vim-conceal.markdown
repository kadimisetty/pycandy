## Unicode Identifiers and vim conceal

1. Identifiers written with Unicode Literals
2. vim conceal feature

Identifiers can be 
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

## Notes
- All identifiers are converted into the normal form NFKC while parsing; comparison of identifiers is based on NFKC.

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
- In interactive interpreter, it stores the result of last evaluation
- Refer to the [`builtins` module](http://docs.python.org/3/library/builtins.html#module-builtins)
- When not in interactive environment, it has no special meaning

`__*__`
: System Defined Names. Definited by Implementations and Interpreters

`__*`
: Class-Private Names



## References
### Documetation
Python 3
- [Lexical Analysis - Identifiers and Keywords](http://docs.python.org/3/reference/lexical_analysis.html#identifiers)
- [unicodedata module](http://docs.python.org/3/library/unicodedata.html#module-unicodedata)
- [Reserved class of Identifiers](http://docs.python.org/3/reference/lexical_analysis.html#reserved-classes-of-identifiers)
- [Keywords](http://docs.python.org/3/reference/lexical_analysis.html#keywords)

Python 2
- [Lexical Analysis](http://docs.python.org/2/reference/lexical_analysis.html#identifiers)

### Further Reading
- [Pros and Cons - Stack Exchange](http://programmers.stackexchange.com/questions/16010/is-it-bad-to-use-unicode-characters-in-variable-names)
- [Valid Identifiers in Non-Normative HTML](http://www.dcl.hpi.uni-potsdam.de/home/loewis/table-3131.html)
