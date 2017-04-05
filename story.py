from action import *
from character import *
from storyText import *
from textToWav import *
from playAudio import *
from collections import *
from story2 import *
import csv

actions = {}
names = {}
tags = {}
story = {}
race = {}
questions = {}
nouns = {}
verbs = {}
sorted_nouns = {}
sorted_verbs = {}
speech = defaultdict(list)
line = defaultdict(list)
tagList = []
perLine = []
other = {}
count = 0

# reads the story
def readStory(objects):


	for id in objects:
		if id >= 1 and id <= 10:

			nouns[id] = objects[id][1]

		elif id >=11 and id <=20:

			verbs[id] = objects[id][1]
		else:
			other[id] = objects[id][1]
	sorted_nouns = sorted(nouns.items(), key=lambda x:x[1])
	sorted_verbs = sorted(verbs.items(), key=lambda x:x[1])


	text = beginStory(sorted_nouns, sorted_verbs, other)
	

	return text





			

		
	






