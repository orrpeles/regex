q# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))? # area code
        {}
                
        )''', re.VERBOSE | re.IGNORECASE)