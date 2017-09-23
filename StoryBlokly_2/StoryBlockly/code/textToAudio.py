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

		if line == "The mouse eats cheese":
			system('say -v Alex ' + str(line) + '.')
			play_wav("../audio/eat.wav")

		elif line == "The cat hisses ":
			system('say -v Alex ' + str(line) +'.')
			play_wav("../audio/meow.wav")

		elif line == "The cat chases The mouse ":
			system('say -v Alex ' + str(line)+'.')
			play_wav("../audio/chase.wav")

		elif line == "The cat explodes":
			system('say -v Alex ' + str(line)+'.')
			play_wav("../audio/explode.wav")

		elif line == "The dragon says hi ":
			system('say -v Alex ' + str(line)+'.')

		elif line == "The turtle says hi":
			system('say -v Alex ' + str(line)+'.')

		elif line == "The dragon dances":
			system('say -v Alex ' + str(line)+'.')
			play_wav("../audio/dance.wav")

		elif line == "The turtle runs":
			system('say -v Alex ' + str(line)+'.')
			play_wav("../audio/chase.wav")

		elif line == "The turtle eats cheese":
			system('say -v Alex ' + str(line)+'.')
			play_wav("../audio/chase.wav")

		elif line == "The dragon dances":
			system('say -v Alex ' + str(line)+'.')
			play_wav("../audio/chase.wav")

		
		

		else:

			system('say -v Alex ' + str(line)+'.')
	
	

	







