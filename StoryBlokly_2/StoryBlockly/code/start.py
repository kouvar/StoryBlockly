import os
import subprocess
from keyHandler import *

key = keyPress()

if key=='s' :
   subprocess.call('../story.py')
