#!/usr/bin/env python3

#import pandas as pd

import pycurl
from io import BytesIO 

days_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(days_of_the_week[2])


b_obj = BytesIO() 
crl = pycurl.Curl() 

# Set URL value
crl.setopt(crl.URL, 'https://wiki.python.org/moin/BeginnersGuide')

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer 
crl.perform() 

# End curl session
crl.close()

# Get the content stored in the BytesIO object (in byte characters) 
get_body = b_obj.getvalue()

# Decode the bytes stored in get_body to HTML and print the result 
print('Output of GET request:\n%s' % get_body.decode('utf8'))


