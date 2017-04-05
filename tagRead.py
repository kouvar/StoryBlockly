import csv
data = []
def tags(filename, nouns, verbs, speech):
	with open(filename, 'wb') as wf:
		writer = csv.writer(wf, delimiter=",")
		writer.writerow(['noun', 'verb','text'])
		for n, v, s in zip(nouns, verbs, speech):
			if s != 0:
				row = [n, v, s]
			else:
				row = [n,v]
			data.append(row)
			writer.writerow(row)
	return data
	