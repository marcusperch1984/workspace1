from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

url = "https://www.biblegateway.com/passage/?search=Ephesians%205:1-16&version=NIV"
html = urlopen(url).read()

variableString = html.decode('utf8')

filename = "my_tmp.txt"
if os.path.exists(filename):
	os.remove(filename)

f = open(filename, "w") # w=over write the contents
f.write(variableString)
f.close()

index = 0
passage_index = 0

with open(filename) as file:
    for line in file:
    	
    	if ("passage-content passage-class" in line):
    		passage_index = index
    		print("INDEX=" + str(index))
    		print(line.rstrip())

    	if index == (passage_index + 1):
    		print(line.rstrip())
    		my_passage = line.rstrip()
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
    		print(text)

    	index = index + 1

if os.path.exists(filename):
	os.remove(filename)

