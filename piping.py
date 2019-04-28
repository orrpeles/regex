import re
heroRegex = re.compile(r'batman|tina fey', re.IGNORECASE)
mo1 = re.search('Batman and tina fey')
mo1.group() # returns batman
mo2 = re.search('tina fey and batman')
mo2.group() # returns tina fey

#another example:
batRegex = re.compile(r'bat(mobile|man|copter)')
mo = batRegex.search('batman lost his hat')
mo.group() # retunrs Batman
mo.group(1) # returns man
