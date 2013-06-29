# modelines

Automatically set options on a per indiviual file basis

## Two forms:
- `[text]{white}{vi:|vim:|ex:}[white]{options}`
- `[text]{white}{vi:|vim:|ex:}[white]se[t] {options}:[text]`

## Example
    /* vim: set ai tw=75: */ ~

## Version targeting
For example, to use a modeline only for Vim 6.0 and later:
	/* vim600: set foldmethod=marker: */ ~
To use a modeline for Vim before version 5.7:
	/* vim<570: set sw=4: */ ~

## Reqs
There can be no blanks between "vim" and the ":".

Note that for the first form all of the rest of the line is used, thus a line
like:
    /* vi:ts=4: */ ~
will give an error message for the trailing `*/`.  This line is OK:
    /* vi:set ts=4: */ ~
