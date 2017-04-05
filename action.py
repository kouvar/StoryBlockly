action = {}
def readVerbs():
	with open('verbs.txt') as verbs:
	 	verb = [line.strip() for line in verbs]
	 	actionWords = [word.split() for word in verb]
	 	for items in actionWords:
	 		
	 		if items[0] == '11' or items[0] == '12':
	 			items[1] = items[1] 
	 			
	 		action[items[0]] = items[1]
	 	return action
	


