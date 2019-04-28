All the regex functions in Python are in the re module. Enter 'import re' into the interactive shell to import this module.
Example:
import re

Python's backslash curse:
'r' marks the string as a raw string , which does not escape characters (in python backslash represents escape characters).
Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing
'\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'

Ref: https://docs.python.org/3/howto/regex.html

Flow:
1.) Import the regex module with import re.
"import re"
2.) Create a Regex object with the re.compile() function (use r' if interested in raw string).
"regObj = re.compile(r'\d')"
3.) Pass the string you want to search into the Regex object’s search() method.
'string = regObj.search("find the digit 8 now")'
4.) Call the Match object’s group() method to return a string of the actual
string.group()
-> matched text. '8'
