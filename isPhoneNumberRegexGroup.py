# this example is identical to isPhoneNumber.py but uses phoneNumRegex
import re #imports regex engine to python
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('number found '+ mo.group()) #Return the string matched by the RE
print('position', mo.span()) #Return a tuple containing the (start, end) positions of the match
mo.group() # returns the number
mo.group(1) # returns 415
mo.group(2) #return 555-4242
mo.groups() #returns a tuple of both groups ('415','555-4242')
areaCode, mainNumber = mo.groups()
areaCode # returns 415
mainNumber # returns 555-4242
