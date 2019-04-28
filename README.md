All the regex functions in Python are in the re module. Enter 'import re' into the interactive shell to import this module.
Example:
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
now phoneNumRegex contains a regex object.

Python's backslash curse:
'r' marks the string as a raw string , which does not escape characters (in python backslash represents escape characters).
Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing
'\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'

The solution is to use Python’s raw string notation for regular expressions; backslashes are not handled in any special way in a string literal prefixed with 'r', so r"\n" is a two-character string containing '\' and 'n',
Ref: https://docs.python.org/3/howto/regex.html
