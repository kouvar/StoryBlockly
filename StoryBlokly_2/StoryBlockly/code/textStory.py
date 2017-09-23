import tuio
import json
from collections import * 



eachLine= {}

text = []
text_lines = []

# Read strings from file 
def readText():
	with open("../text_data/tagNames.txt", "rb") as wf:
		lines = [line.strip() for line in wf]
		words = [word.split() for word in lines]
		for word in words:
			eachLine[word[0]] = ' '.join(word[1:])
			
			

	return eachLine
	
# Generate text for each line of the program 

def generateText(programLines):

	eachLine= readText()
	for line in programLines:
		print line
		text.append(eachLine[line[0]])
			
	text_lines.append(' '.join(text))		
	return text_lines



	