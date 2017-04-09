import tuio
import ast
import collections
from collections import * 
import json
import textStory
from textStory import * 

nouns = defaultdict(list)
verbs = defaultdict(list)
other = defaultdict(list)
structure = []
program = []
loopStartIndex = 0
loopEndIndex = 0
branchStartIndex = 0
branchEndIndex = 0
loopCount = 0
loopCounter = 0

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

#  Determines if the tag is a noun, verb or other[loop, branch].Do we need this??
def tagType(objects):
	for obj in objects:

		if int(obj) in range(1,11) and obj not in nouns:
			nouns[obj].append([objects[obj][0],objects[obj][1]]) #not sure why I am craeting another dictionary of lists, can I just make a list of objects?
		elif int(obj) in range(11, 21) and obj not in verbs:
			verbs[obj].append([objects[obj][0],objects[obj][1]])
		else:
			other[obj].append([objects[obj][0],objects[obj][1]])
	
	return nouns, verbs, other
# Sorting tags by y value 
def sortTagsY(tags): 
	
	tagsSortedY = sorted(tags.items(), key=lambda x:x[1][0][1])
	
	return tagsSortedY

# Sorting tags by x value 
def sortTagsX(tags):
	tagsSortedX = sorted( tags, key=lambda x:x[1][0][0])
	return tagsSortedX

# Determine each line of the story and the tags it contains
def lineOfStory(sortedNouns, sortedVerbs, sortedOther):
	if not sortedOther:
		for noun, verb in zip(sortedNouns, sortedVerbs):
			
			if (noun[1][0][1] - verb[1][0][1]) < 0 :
				structure.append(sortTagsX([noun, verb]))
	else:
		for noun,verb,other in zip(sortedNouns, sortedVerbs, sortedOther):
			
			
						
	
	
	
	
	return structure

# Determine programming concept associuated with each array and create a data structure for the entire program
def programConcept(programStructure):
	global loopStartIndex, loopEndIndex, branchStartIndex, branchEndIndex, count
	for line in programStructure:
		if ('21' in line) and (count % 2 == 0):
			loopStartIndex = programStructure.index(line)
			count += 1
		elif ('22' in line) and (count % 2 == 1):
			loopEndIndex = programStructure.index(line)
			count += 1
		elif ('23' in line) and (counter % 2 == 0):
			branchStartIndex = programStructure.index(line)
			counter += 1
		elif ('24' in line) and (counter % 2 == 1):
			branchEndIndex = programStructure.index(line)
			counter += 1

	for i in range(0, len(programStructure)):
		if i == loopStartIndex:

			for j in range(0,3):
				while i <= loopEndIndex:
					program.append(programStructure[i])
					i = i + 1
	
		elif i != loopStartIndex or i != loopEndIndex:
			program.append(programStructure[i])	
	return program

tagDict = readTags()
#print tagDict
nouns, verbs, other = tagType(tagDict)

sortedNouns = sortTagsY(nouns)

sortedVerbs = sortTagsY(verbs)
sortedOther = sortTagsY(other) 

programStructure = lineOfStory(sortedNouns, sortedVerbs, sortedOther)

program = programConcept(programStructure)

generateText(program)
