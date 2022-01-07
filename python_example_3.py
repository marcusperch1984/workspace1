#!/usr/bin/env python3

#import pandas as pd

# sudo apt-get install python-pycurl
import pycurl
from io import BytesIO 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

days_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(days_of_the_week[2])


b_obj = BytesIO() 
crl = pycurl.Curl() 

# Set URL value
#crl.setopt(crl.URL, 'https://www.bbc.co.uk/news/topics/c9qdqqkgz27t/ftse-100')
crl.setopt(crl.URL, 'https://www.biblegateway.com/passage/?search=Ephesians%205:1-2&version=NIV')

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

variableString = get_body.decode('utf8')

print(variableString)
print("did it work?")


