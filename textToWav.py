from os import system
import wave
import sys
import os.path
import time

from playAudio import *

# converts the text to speech using the voice to a wav file
def convertToWav(text):
	for line in text:
		if line == "Dragon talk":
			system('say -r 500 -v Bad  Hi!! I am curly. I will win the race.')
		elif line == "Firegirl talk":
			#system('say -v Alex ' + str(line))
		elif line == "Robot talk":
			#system('say -v Alex' + str(line))
			system('say -r 300 -v Cellos Hi!! I am ozi. I run like the wind!')
		elif line == "Dragon runs":
			system('say - v Alex ' + str(line))
			play_wav("dragon.wav")
		elif line == "Firegirl runs":
			system('say -v Alex ' + str(line))
			play_wav("firegirl.wav")
		elif line == "Robot runs":
			system('say -v Alex ' + str(line))
			play_wav("robot.wav")

		elif line == "Dragon dances":
			system('say -v Alex ' + str(line))
			#play()
		elif line == "Firegirl dances":
			system('say -v Alex ' + str(line))
			#play()
		elif line == "Robot dances":
			system('say -v Alex' + str(line))
			#play()
		elif line == "Dragon eats":
			system('say -v Alex' + str(line))
			play_wav("burger.wav")
		elif line == "Firegirl eats":
			system('say -v Alex' + str(line))
			play_wav("burger.wav")
		elif line == "Robot eats":
			system('say -v Alex' + str(line))
			play_wav("burger.wav")
		else:

			system('say - v Alex' + str(line))

	







