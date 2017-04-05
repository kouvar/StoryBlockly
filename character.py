character = {}
def readNoun():
    with open('nouns.txt') as desc:
        nouns = [line.strip() for line in desc]
        noun = [word.split() for word in nouns]
        for item in noun:
        	if item[0] not in character:
        		character[item[0]] = item[1]
    return character



