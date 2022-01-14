from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

# variable 

'''
Define a variable

If this was C/C++ language

LOGIC:
bool a = false 		# boolean can only b true or false

NUMBERS:
uint8_t i = 0 		# if its a positive number between 0-255 [unsigned]
int8_t i = 0		# if it could negative and positive -128 to +127 
..
uint64_t ... etc

STRINGS:
h e l l o = 5 bytes
h=8 bits
e=8 bits
l=9 bits
l=8 bits
o=8 bits

thin of "char" [character] as equivalent to 1 byte

char a = "h";
char word[5];
				// byte format
word[0] = "h"; 	// 0x68
word[1] = "e";	// 0x65
word[2] = "l";	//
word[3] = "l";	//
word[4] = "o";	// 
strcpy(word, "this text") etc
'''

# [1] GET DATA FROM WEBSITE
url = "https://www.biblegateway.com/passage/?search=Ephesians%202:1-8&version=NIV"
html = urlopen(url).read() # byte format

variableString = html.decode('utf8') # convert data from a number to a text

# [2] SAVE DATA TO A FILE SO WE CAN PLAY WITH IT
filename = "my_tmp.txt"
if os.path.exists(filename):
	os.remove(filename)

f = open(filename, "w") # w=over write the contents
f.write(variableString)
f.close()

index = 0
passage_index = 0

# [3] READ THE FILE LINE BY LINE
with open(filename) as file:
    for line in file:
    	

    	# DETECT PATTERN
    	if ("passage-content passage-class" in line):
    		passage_index = index
    		print("INDEX=" + str(index))
    		print(line.rstrip())


    	if index == (passage_index + 1):

    		# PATTERN HAS NOW BEEN DETECTED AND WE HAVE THE USEFUL INFO
    		print(line.rstrip())
    		my_passage = line.rstrip()

    		# FILER OUT STUFF LIKE <html>
    		soup = BeautifulSoup(my_passage, features="html.parser")

    		# kill all script and style elements
    		for script in soup(["script", "style"]):
    			script.extract()    # rip it out

    		text = soup.get_text()
    		# break into lines and remove leading and trailing space on each
    		lines = (line.strip() for line in text.splitlines())
    		# break multi-headlines into a line each
    		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    		# drop blank lines
    		text = '\n'.join(chunk for chunk in chunks if chunk)

    		# CLEAN TEXT TP PRINT
    		print(text)

    	index = index + 1

if os.path.exists(filename):
	os.remove(filename)

