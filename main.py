import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import functions

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def assistant():
    with sr.Microphone() as source:
        print("Проверяю фоновые звуки")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Спроси меня о чем угодно')
        recordedaudio=recognizer.listen(source)
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        if 'sam' in text:
            print('Your message:',format(text))
            if ('chrome' in text) or ('play' in text) or ('youtube' in text):
                functions.browser(text)
            elif 'time' in text:
                functions.check_time(text)
            elif 'wiki' in text:
                functions.wikipedia(text)
            elif 'exit' in text:
                txt = 'Thanks for using Sam Voice Assistant. Have a nice day'
                engine.say(txt)
                engine.runAndWait()
                quit()
            else:
                pass


while True:
    assistant()