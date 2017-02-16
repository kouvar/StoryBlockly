import pyaudio
import wave
import sys
import os.path
import time
import csv
from os import system

CHUNK_SIZE = 1024
char_info = {}

def play_wav(wav_filename, chunk_size=CHUNK_SIZE):
    
    # Play wav file
    try:
        print 'Trying to play file ' + wav_filename
        wf = wave.open(wav_filename, 'rb')
    except IOError as ioe:
        sys.stderr.write('IOError on file ' + wav_filename + '\n' + \
        str(ioe) + '. Skipping.\n')
        return
    except EOFError as eofe:
        sys.stderr.write('EOFError on file ' + wav_filename + '\n' + \
        str(eofe) + '. Skipping.\n')
        return

    # Instantiate PyAudio.
    p = pyaudio.PyAudio()

    # Open stream.
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(chunk_size)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(chunk_size)

    # Stop stream.
    stream.stop_stream()
    stream.close()

    # Close PyAudio.

    p.terminate()
text = {}
class character(object):
    # Character voices
    def __init__(self, id, voice):
        self.cid = id
        self.voice = voice
    #reading voice
    def readVoice(self):
        with open('characters.txt') as rf:
            content = [line.strip() for line in rf]
            for words in content:
                text[words[0]] = words[1:]
            for ids in text:
                if int(ids) == self.cid:
                    system('say -v '+self.voice+' '+ text[str(self.cid)])

            
            #voiceText = ' '.join(text[1:])
            #print voiceText
            #system('say -v '+self.voice+' '+str(voiceText))







king = character(3, 'Alex')
king.readVoice()
knight = character(6, 'Fred')
knight.readVoice()


