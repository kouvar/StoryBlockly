# Reads a file and returns teh story text as a list
story = dict()
pre= []
race = {}
qs = {}
def storyText():
    with open('speechText.txt') as desc:
        stories = [line.strip() for line in desc]
        story1 = [word.split() for word in stories]
        for line in story1:
        	if len(line) == 2:
        		story[line[0]] = line[1]
    return story
        		


			


def raceText():
	with open('raceText.txt') as raceRead:
		race = [line.strip() for line in raceRead]
	return race
def questionText():
	with open('questions.txt') as qRead:
		questions = [line.strip for line in qRead]
	return questions
