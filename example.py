import tuio

from track import *
import keyHandler
from keyHandler import *
from character import *
from story import *
from collections import *
from tagRead import *
from story2 import *
import threading
from threading import * 


objList = {}
nounList = defaultdict(list)
verbList = defaultdict(list)
speechList = defaultdict(list)
tagList =[]
tracking = tuio.Tracking()
count = 0


print "loaded profiles:", tracking.profiles.keys()
print "list functions to access tracked objects:", tracking.get_helpers()





'''def track():
	global objList
	tracking.update()
	for obj in tracking.objects():
		objList = tagTracking(obj.id, obj.xpos, obj.ypos)
	print objList

threading.Timer(1, track)'''

while 1:
	try:
		keypressed = True
		key = keyPress()
		if keypressed and key == " ":
			
			keypressed = False
		tracking.update()
		for obj in tracking.objects():
			objList = tagTracking(obj.id, obj.xpos, obj.ypos)
		text = readStory(objList)
		
		
		
		convertToWav(text)
	except:
		print "error"
