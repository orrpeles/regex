# this example is identical to isPhoneNumber.py but uses phoneNumRegex
import re #imports regex engine to python
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('number found '+ mo.group()) #Return the string matched by the RE
print('position', mo.span()) #Return a tuple containing the (start, end) positions of the match
