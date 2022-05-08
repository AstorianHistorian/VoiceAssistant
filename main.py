
import speech_recognition as sr 
"""
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
"""
import functions as f


def assistant():
    with sr.Microphone() as source:
        f.recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything')
        raudio=f.recognizer.listen(source)
        try:
            text=f.recognizer.recognize_google(raudio,language='en_US')
            text=text.lower()
            if 'sam' in text:
                print('Your message:',format(text))
                if ('chrome' in text) or ('play' in text) or ('youtube' in text):
                    f.browser(text)
                elif 'time' in text:
                    f.check_time(text)
                elif 'wiki' in text:
                    f.wikipedia(text)
                elif 'exit' in text:
                    txt = 'Thanks for using Sam Voice Assistant. Have a nice day'
                    f.engine.say(txt)
                    f.engine.runAndWait()
                    exit()
                else:
                    pass
        except:
            pass


while True:
    assistant()