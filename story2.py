from character import *
from action import *
from storyText import *
from textToWav import *
import csv
from os import system

names = {}
actions = {}
story = {}
race = {}
questions = {}
noun_text = {}
verb_text = {}
otherText = {}
noun2 = {}
verb2={}
text = []
counter = 0
new_text = []
listToString=""

 
def beginStory(nouns, verbs, other):

	names = readNoun()
	actions = readVerbs()
	race = raceText()
	story = storyText()
	questions = questionText()
	noun2 = nouns
	verb2 = verbs
	otherText = other
	count = 0

	
	for noun, verb in zip(noun2, verb2):
		global stxt 
		if noun[0] not in text and verb[0] not in text:




			text.append([names[str(noun[0])], actions[str(verb[0])]])
			

	for line in text:
		if line != "":
			listToString = ' '.join(line)
			if line not in new_text:

				new_text.append(listToString)
	
	return  list(set(new_text))

	

	


		
	

	#convertToWav(' '.join(text))
