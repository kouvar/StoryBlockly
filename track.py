# Reads the tag in the current frame and add it to a list
import tuio
objList= {}
def tagAppear(id, x, y):
	if id not in objList:
	
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


def tagTracking(id, x, y):
	tagMove(id,x,y)
	objects = tagAppear(id,x,y)
	
	return objects
	