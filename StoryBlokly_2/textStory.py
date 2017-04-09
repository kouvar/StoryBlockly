import tuio
import json
from collections import * 


nouns = {}
verbs = {}
text = []

# Read strings from file 
def readText():
	with open("tagNames.txt", "rb") as wf:
		lines = [line.strip() for line in wf]
		words = [word.split() for word in lines]
		for word in words:
			if int(word[0]) in range(0,11):
				nouns[word[0]] = word[1]
			elif int(word[0]) in range(11,21):
				verbs[word[0]] = word[1]
	return nouns, verbs
	
# Generate text for each line of the program 

def generateText(programLines):
	noun, verb = readText()
	for line in programLines:
		for word in line:
			if word[0] in noun:
				character = noun[word[0]]
			elif word[0] in verb: 
				action = verb[word[0]]
		text.append(' '.join([character, action]))






	