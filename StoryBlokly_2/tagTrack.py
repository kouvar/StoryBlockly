import tuio
import json


import threading
from threading import *

tracking = tuio.Tracking()
print "loaded profiles:", tracking.profiles.keys()
print "list functions to access tracked objects:", tracking.get_helpers()

objList= {}
row = []
objectList = {}

# Reads tag id, x co-ordinate anad y co-ordinate values into a dictionary of lists
def tagAppear(id, x, y):
	if id not in objList and id != "":
	
		objList.setdefault(id, [])
		objList[id].append(x)
		objList[id].append(y)
	return objList

# Keeps track of the tag with x and y co-ordinates if the tag moves
def tagMove(id, x, y):
	
	if id in objList:
		if objList[id][0] - x != 0:
			objList[id][0] = x
		if objList[id][1] - y != 0:
			objList[id][1] = y
		
	else:
		tagAppear(id,x,y)

# Keeps track of visible and moving tags
def tagTracking(id, x, y):
	tagMove(id, x, y)
	objects = tagAppear(id, x, y)
	return objects

# Writing all the visible tags stiored as a dictionary to a json file 
'''def writeToFile(objectList):

	with open("tags.txt", "w") as wf:
		json.dump(objectList, wf)'''
		

def track():
	try: 
		tracking.update()
		for obj in tracking.objects():
			objectList = tagTracking(obj.id, obj.xpos, obj.ypos)
		
			json.dump(objectList, open("tags.txt",'w'))
			
			#writeToFile(objectList)
	except KeyboardInterrupt:
		tracking.stop()

while 1:
	track()

