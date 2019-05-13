#!/bin/python
# script that finds  matches of emails or numbers from clipboard using regex
# ref: phone_email_extractor.ipynb

# preparations:
# 1.) Import relevant libraries
# 2.) Prepare number extractor regex
# 3.) Prepare email extractor regex
# 4.) Prepare object with the pasted clipboard text

import re, pyperclip # 1.)

phoneRegexSimple = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)') # 2.) number extractor regex
emailRegex = re.compile(r'''(
[a-z,A-Z,0-9.%_+-]+      # username alphanumeric -> character class followed by one or more chars
@                        # @
[a-z,A-Z,0-9_-]+         # domain alphanumeric
\.\w{2,6}          # dot and some alpha ending
)''', re.VERBOSE) # 3.) email extractor regex

text = str(pyperclip.paste()) # object taking copied text on clipboard # 4.)

allMatches = []
for phones in phoneRegexSimple.findall(text):
    phoneMatch = '-'.join([phones[1], phones[3], phones[5]])
    allMatches.append(phoneMatch)
for emails in emailRegex.findall(text):
    allMatches.append(emails)

if len(allMatches) > 0:
    pyperclip.copy('\n'.join(allMatches))
    print('copied to clipboard')
    print('\n'.join(allMatches))
else:
    print('no match found')



