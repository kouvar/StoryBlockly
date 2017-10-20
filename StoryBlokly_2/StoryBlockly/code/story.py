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
program = []
branchStart= False
branchEnd= False
newLine = []
lines= []
left_tags=[]

# list of all tags. Right now I have unique tags for every piece
nouns = {0,1,2,3,4,5,6,7,8,9,10,21, 22, 23, 24, 25, 26, 34, 35, 55}
others={35,36}
verbs = {11,12,13,14,15,16,17,18,19,20,27, 28, 29, 30}
goto = {31, 32} # This is a loop
branch = {33}
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




# Checks and finds all tags to the right. 
def compare(x, sort_tags):

	global newLine
	
	for i in range(sort_tags.index(x), len(sort_tags)):
		
		if x[1][1] - sort_tags[i][1][1] <= 0.08:
			
			if sort_tags[i] not in newLine:
				newLine.append(sort_tags[i])	
	
	return newLine
	
	'''global newLine
	for  i in range(sorted_tags.index(x), len(sorted_tags)):

		if abs(x[1][1] - sorted_tags[i][1][1]) <=0.0855: # Threshold to find rightmost tags
#			print x, x[1][1] - sorted_tags[i][1][1]
			if sorted_tags[i] not in newLine:
				newLine.append(sorted_tags[i])
	if newLine not in increment:
		increment.append(newLine)
	
	return increment'''

	


# Find nouns and sorted them on Y values then find tags that are in the same row


def tagType(tagDict):
	line = []
	sorted_tags=[]
	sortedYtags = sortTagsY(tagDict)
	
	# removing all left tags and make a list of them
	'''for tag in sortedYtags:
		if  tag[1][0] < .95 and tag[1][0] > .5:
			left_tags.append(tag)
			del tagDict[tag[0]]
		# right side tags	
		else:
			sorted_tags.append(tag)
	# find out tags closest to left tags
	for tag in left_tags:
		line= compare(tag, sorted_tags)
		
		
		if line not in lines:
			lines.append(line)
	# removing right tags
		
				
	'''	
	for tag in sortedYtags:

		if  tag[1][0] < .95 and tag[1][0] > .12:

			line = compare(tag, sortedYtags)
		if line not in lines:
			lines.append(line)
		

	
	return lines
	

# Detrmine the actual lines of the story from the sorted rows. Make changes to lines to add loops and branches. 
def linesForText(lines):
	global chunk 
	chunk = []
	div_lines = []
	global branchStart, branchEnd
	global gotoStart, loop
	loop = False
	gotoStart = -1
	gotoEnd = -1
	
	flat_line = [tag for line in lines for tag in line ]

	for tag in flat_line:
		if int(tag[0]) == 31:
			loop=True
			gotoStart = flat_line.index(tag)
		elif int(tag[0]) == 32:
			gotoEnd = flat_line.index(tag)
		elif int(tag[0]) == 33:
			branchStart = True
			branchIndex = flat_line.index(tag)


	for i in range(len(flat_line)):
		if not branchStart and not branchEnd:
			if int(flat_line[i][0]) == 32 and loop:
				intermediate =[]
				for k in range(0,2):
					for j in range(gotoStart+1, gotoEnd):
						
						intermediate.append(flat_line[j])

					loop = False
				chunk.append(intermediate)
				
			elif not loop and (int(flat_line[i][0]) != 31 or int(flat_line[i][0]) != 32):
				chunk.append(flat_line[i])
		
				
		elif branchStart and not branchEnd and not loop:
			for i in range(branchIndex):
				chunk.append(flat_line[i])
			for i in range(branchIndex, len(flat_line)):
				chunk.append(flat_line[i])
				branchEnd = True

	#print text_Lines
	print chunk
	return chunk

#system('say Say start to start the story')
def finalLines(chunk):
	left_tags=[]
	right_tags=[]
	branch_tag=[]
	final = []
	line=[]
	for tag in chunk:
		if type(tag)!=list:
			if int(tag[0]) in nouns  and abs(tag[1][0] - tag[1][1])< 0.5:
				left_tags.append(tag)
		else:
			if int(tag[0][0]) in nouns  and abs(tag[0][1][0] - tag[0][1][1])< 0.5:
				left_tags.append(tag)
		
	for tag in left_tags:
		line=[]
		for t in chunk:
			if type(t) != list:
				if (tag[1][0] - t[1][0]) >=0 and (tag[1][0] - t[1][0]) <0.3 and (tag[1][1] - t[1][1])>=0 and (tag[1][1] - t[1][1]) <0.06:
				
					line.append(t)
			else:
				line.append(t)
				final.append(line)
		for value in line:
			chunk.remove(value)
		if line not in final:
			final.append(line)

	return final
		


		

	


tagDict = readTags()
program = tagType(tagDict)
textLines = linesForText(program)
final = finalLines(textLines)
text = generateText(final) # found in textStory.py
print text
convertToWav(text) # found in textToAudio.py
	
