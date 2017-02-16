import tuio

import keyHandler
from keyHandler import *
import character
from character import *
objList = {}
tracking = tuio.Tracking()
print "loaded profiles:", tracking.profiles.keys()
print "list functions to access tracked objects:", tracking.get_helpers()

def tagAppear(id, x, y):
	if id not in objList:
		objList.setdefault(id, [])
		objList[id].append(x)
		objList[id].append(y)
		if id == 3:
			king = character(id, 'Alex')
		elif id == 6:
			knight = character(id, 'Fred')


def tagMove(id, x, y):
	if id in objList:
		if objList[id][0] - x != 0:
			objList[id][0] = x
		if objList[id][1] - y != 0:
			objList[id][1] = y
	else:
		tagAppear(id,x,y)



try:

	while 1:
		if keyPress() == 'a':
			while 1:
				tracking.update()
				for obj in tracking.objects():
					

					tagAppear(obj.id, obj.xpos, obj.ypos)
					tagMove(obj.id, obj.xpos, obj.ypos)
					for ob in objList:
						print ob, objList[ob][0], objList[ob][1]
						king.readVoice()
						knight.readVoice()
		elif keyPress() =='s':
			tracking.stop()
		

            		


except KeyboardInterrupt:
	tracking.stop()








 
