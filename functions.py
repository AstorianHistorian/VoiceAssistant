import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def browser(text):
    if 'chrome'in text:
        txt='Opening chrome..'
        engine.say(txt)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    elif 'play' in text:
        txt='Opening youtube..'
        engine.say(txt)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    elif 'youtube' in text:
        txt='Opening youtube..'
        engine.say(txt)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')

def check_time(text):
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    engine.say(time)
    engine.runAndWait()

def wikipedia(text):
    b='Opening Wikipedia..'
    engine.say(b)
    text = text.split('search')
    webbrowser.open(f'https://en.wikipedia.org/w/index.php?search={text[1]}')