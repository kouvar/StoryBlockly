import tuio
import json
from collections import * 



eachLine= {}
text_line =[]

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
		text=[]
		lines=[]

		for word in line:
			text.append(eachLine[word[0]])
		
		print text
		text_line.append(' '.join(text))

	
	text_lines.append(text_line)
	
	return text_line



	