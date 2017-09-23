import tuio
import ast
import collections
from collections import * 
import json
import textStory
from textStory import * 
from textToAudio import *
from keyHandler import *
from os import system

nouns = defaultdict(list)
verbs = defaultdict(list)
other = defaultdict(list)
structure = []
program = []
loopStartIndex = 0
loopEndIndex = 0
branchStart= False
branchEnd= False
loopCount = 0
loopCounter = 0
counter = 0
lineList = []
storyLines = []
lines= []
loopLine=[]
increment=[]
nouns = {0,1,2,3,4,5,6,7,8,9,10,21, 22, 23, 24, 25, 26}
verbs = {11,12,13,14,15,16,17,18,19,20,27, 28, 29, 30}
goto = {31, 32}
branch = {33, 34}
#nouns, verbs, other = readText()


# Converts unicode dictionary keys to strings
def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data
#  Reads tags from the json file generated from tagTrack.py
def readTags():
	with open("tags.txt") as data_file:
		objects = json.load(data_file)
		objects = convert(objects)

	return  objects


	# Sorting tags by y value 
def sortTagsY(tags): 
	tagsSortedY = sorted(tags.items(), key=lambda x:x[1][1], reverse=True)
	
	
	return tagsSortedY

# Sorting tags by x value 
def sortTagsX(tags):
	tagsSortedX = sorted(tags, key=lambda x:x[1][0], reverse=True)
	return tagsSortedX





def compare(x, sorted_tags):
	newLine = []


	for  i in range(sorted_tags.index(x), len(sorted_tags)):
		if x[1][1] - sorted_tags[i][1][1] <=0.8:
#			print x, x[1][1] - sorted_tags[i][1][1]
				
			newLine.append(sorted_tags[i])
				
		
	return newLine



def tagType(tagDict):
	line = []
	sortedYtags = sortTagsY(tagDict)
	keyC = False
	keyM = False
	loopTag = True
	branchTag = True
	for tag in sortedYtags:
		

	
		if int(tag[0]) in nouns:
			if  tag[1][0] < .95 and tag[1][0] > .12:
				line = compare(tag, sortedYtags)

			if line not in lines:
				lines.append(line)

	return lines


def linesForText(lines):
	chunk = []
	global branchStart, branchEnd
	flat_line = [tag for line in lines for tag in line ]
	for tag in flat_line:
		if int(tag[0]) == 32:
			gotoStart = flat_line.index(tag)
		elif int(tag[0]) == 31:
			gotoEnd = flat_line.index(tag)
		elif int(tag[0]) == 40 or int(tag[0]) == 44:
			branchStart = True


	for i in range(len(flat_line)):
		if not branchStart and not branchEnd:
	
			if  int(flat_line[i][0]) == 31:
				for j in range(gotoStart, gotoEnd):
					chunk.append(flat_line[j])
			else:
				if int(flat_line[i][0]) != 32:
					chunk.append(flat_line[i])


		elif branchStart and not barnchEnd and int(flat_line[i][0]) == 54  or int(flat_line[i][0]) == 55:
			chunk.append(flat_line[i])
			branchEnd = True

		
			

	print chunk
	return chunk

#system('say Say start to start the story')
key = keyPress()
if key == 's':


	tagDict = readTags()
	program = tagType(tagDict)
	textLines = linesForText(program)

	text = generateText(textLines)
	print text
	convertToWav(text)
	
