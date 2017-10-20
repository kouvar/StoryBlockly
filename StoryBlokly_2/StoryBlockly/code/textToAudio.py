from os import system
import wave
import sys
import os.path
import time
from keyHandler import *
from playAudio import *

# converts the text to speech using the voice to a wav file. Checks if each line matches the line of the story. 
def convertToWav(text):
	for line in text:

		if line == "Mouse eats cheese":
			system('say -v Junior ' + str(line) + '.')
			play_wav("../audio/eat.wav")

		elif line == "Cat hisses":
			system('say -v Junior ' + str(line) +'.')
			play_wav("../audio/meow.wav")
		elif line == "Cat says hi":
			system('say -v Junior ' + str(line) +'.')
			play_wav("../audio/meow.wav")

		elif line == "Cat chases Mouse":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/chase.wav")
		elif line == "Cat runs after Mouse":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/chase.wav")
		elif line == "Cat eats Mouse":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/eat.wav")

		elif line == "Mouse runs after":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/chase.wav")

		elif line == "Cat dances":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/dance.wav")	

		elif line == "Cat explodes":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/explode.wav")

		elif line == "Dragon explodes":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/explode.wav")

		elif line == "Dragon says hi ":
			system('say -v Junior ' + str(line)+'.')

		elif line == "The turtle says hi":
			system('say -v Junior ' + str(line)+'.')

		elif line == "Dragon dances":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/dance.wav")
		elif line == "Turtle dances":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/dance.wav")
		elif line == "Mouse chases Cat":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/chase.wav")

		elif line == "Turtle runs after Dragon":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/chase.wav")
		elif line == "Dragon runs after Turtle":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/chase.wav")
		elif line == "Cat runs after":
			system('say -v Junior ' + str(line)+'.')
			play_wav("../audio/chase.wav")

		elif line == "Turtle eats cheese":
			system('say -v Alex ' + str(line)+'.')
			play_wav("../audio/eat.wav")

		
		elif line == "Dragon dances Dragon dances":
			system('say -v Alex ' + str(line)+'.')
			play_wav("../audio/dance.wav")
		elif line == "Dragon chases Dragon chases":
			system('say -v Alex ' + str(line)+'.')
			play_wav("../audio/chase.wav")
		elif line == "Dragon runs after Dragon runs after":
			system('say -v Alex ' + str(line)+'.')
			play_wav("../audio/chase.wav")






		
		

		else:

			system('say -v Alex ' + str(line)+'.')

		time.sleep(0.4)
	

	







