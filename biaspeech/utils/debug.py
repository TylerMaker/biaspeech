# --------------------------
# Utils folder
#
# Debug, lines to paste in the interpreter
# --------------------------

""" text to speech """
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', 'french')
engine.say("salut beau gosse") # say some
engine.runAndWait() # go
engine.stop() # stop
            
""" speech to text """
import speech_recognition as sr 
import sounddevice
recognizer = sr.Recognizer() # initialize the recognizer    
r = sr.Recognizer()                                                                                   
mic = sr.Microphone(device_index=1)
with mic as source: # set the deviceIndex                                                              
    recognizer.adjust_for_ambient_noise(source, duration=1) # w adjust duration
    recorded_audio = recognizer.listen(source) # listen
    text = recognizer.recognize_google(recorded_audio, language="fr") # w language
    print(format(text)) # format

""" translate """
from translate import Translator
from langdetect import detect
from langdetect import DetectorFactory

text="quelle est la capitale de la france"
translator= Translator(from_lang="fr", to_lang="en")
result = translator.translate(text)
print(result)

result = detect(text)
print(result)

""" serial python to arduino """
import serial
import time

arduino = serial.Serial(port='/dev/cu.usbserial-1460',  baudrate=115200, timeout=.1)
time.sleep(1.5)
arduino.write(bytes('sing1', 'utf-8'))

""" python polymorph """
import os
os.environ['OPENAI_API_KEY'] = "_OPENAI_API_KEY" # openAI API key
os.environ['OS'] = "_OS"
os.environ['ARDUINO'] = ""

from controllers.base import Controller
import logging
import logging.config

controller = Controller()

