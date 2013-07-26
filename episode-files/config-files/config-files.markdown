# Configuration Files
Saving data to and from configuration files


## Common Configuration File Formats
- Native data types like dictionaries, lists etc.
- INI
- JSON
- shlex
- yaml


## Relevant Libraries
stdlib:
- ConfigParser
- json
- shlex

external:
- ConfigObjects
- pyyaml


## Config Parser
- Tutorial
- Workflow
- Options
- Exception Kinds
- [Customising the Parser][parsercust]

## INI files
- Ignore lines _beginning_ with a semi-colon ";", pound sign "#", ( and in other languages - the case-insenstive letters "REM")
    - REM stands for "Remark" and is not part of the Python default commenting prefixes
- Use above for comments
- By default 3.0 has inline commenting disabled
- In regular INI file handling, when writing to an INI file, all commetns are wiped out
- [Commonly used extenstions for language independent INI files][wiki-ini-files] are the `.CFG`, `.conf`, `txt` eg: `config.txt`


## Notes about INIs
- Doesnt supprt arbitrarily complex files and nesting
- Doesnt have standard mechanis for encoding data
- XML, JSON, YAML are also better alternatives but all three come with
  significant syntax weight hits.

- By default empty lines are party of the same key's value and the value
  extends to include any indented lines, which might cause an error, so the
  consider empty values features is suggested to be disabled.  

- Default Section
    - The config parser by default, allows a `default_section` which by default
    is set to: `DEFAULT`
    - This section is normally called default but can be changed, even at
    runtime by setting that attribute
    - The common values are `general` or `common`
    - Modifiable attribute of parser is `parser_instance.default_section` and
    can be set at run time to convert between file formats for instance.

- Interpolation
    - `configparser.BasicInterpolation` & `configparser.ExtendedInterpolation`
    - Accesed from attribute -  `configparser.BasicInterpolation`
    - [Python Doc Interpolations - ConfigParser][interpolation]
    - Can be turned off by letting the attribute above be `None`
    - `ExtendedInterpolation()` can be used to have a more advaned parser with more features
    - Values can be used to include value of key from above, eg: 
        ```python
            [Paths]
            home_dir: /Users
            my_dir: %(home_dir)s/lumberjack
            my_pictures: %(my_dir)s/Pictures
        ```

- `configparser.BOOLEAN_STATES`
    - default true values are `1`, `yes`, `true` and `on`. default false values are `0`, `no`, `false` and `off`
    - represented by attribute above and can be changed to, for example, mean yes with `hellyeah`

- `configparser.optionxform(option)`
    - default sets the key to lowercase
    - It can be changed to perform a `lambda` on the key when reading it so it is read as the processed key.

- Other important attributes of ConfigParser


## ConfigParser.Objects

Sending options to the ConfigParser

    ```python
    class configparser.ConfigParser(defaults=None,
            dict_type=collections.OrderedDict,
            allow_no_value=False,
            delimiters=('=', ':'),
            comment_prefixes=('#', ';'),
            inline_comment_prefixes=None,
            strict=True,
            empty_lines_in_values=True,
            default_section=configparser.DEFAULTSECT,
            interpolation=BasicInterpolation())
    ```


## ConfigParser Exceptions
- configparser.Error
- configparser.NoSectionError
- configparser.DuplicateSectionError
- configparser.DuplicateOptionError
- configparser.NoOptionError
- configparser.InterpolationError
- configparser.InterpolationDepthError
- configparser.InterpolationMissingOptionError
- configparser.InterpolationSyntaxError
- configparser.MissingSectionHeaderError
- configparser.ParsingError


## Customising ConfigParser behavior
- As there are many INI file formats since it
is not very well standardised, Python allows
config parser to be customised to accomodate many
configurations
- The `configparser.RawConfigParser` has basic defaults that can be used to customise.


## References
[parsercust]: http://docs.python.org/3.3/library/configparser.html#customizing-parser-behaviour
[wiki-ini-files]: http://en.wikipedia.org/wiki/INI_file
[interpolation]: http://docs.python.org/3/library/configparser.html#interpolation-of-values
