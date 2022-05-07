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
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))
        if ('chrome' in text or 'play' in text or 'youtube' in text):
            functions.browser(text)
        elif 'time' in text:
            functions.check_time(text)
        elif 'wiki' in text:
            functions.wikipedia(text)
        elif 'exit' in text:
            a = 'Thanks for using Liara Voice Assistant. Have a nice day'
            engine.say(a)
            engine.runAndWait()
            quit()
    except Exception as ex:
            print(ex)


while True:
    assistant()