import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import smtplib
from google.cloud import translate
# import cv2
# from ecapture import ecapture as ec
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#print(voices[3].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Vishal")
    elif hour>=12 and hour<16:
        speak("Good Afternoon! Vishal")
    elif hour>=16 and hour<20:
        speak("Good evening! Vishal")
    else:
        speak("Good Night! Vishal")

    speak("Jarvis here! How can I help you?")

def sendEmail(to, content):
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('vishal.pentakota10@gmail.com', 'Vishal@10')
    server.sendmail('vishal.pentakota10@gmail.com',to,content)
    server.close()

def takeCommand():
    #Miprophone inputs
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e):
        print("Say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak('searching Wikipedia...')
            query=query.replace("Wikipedia", "")
            results = wikipedia.summary(query,sentences=4)
            speak(results)
            #print(results)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'play music' in query:
            webbrowser.open("www.spotify.com")
        elif 'play songs' in query:
            music_dir= 'D:\\songs'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Vishal, the time is {strTime}")
        elif 'send email to srihari' in query:
            try:
                speak("What is the message?")
                content = takeCommand()
                to = "srihariece1@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Failed to send!")
        # elif 'take a picture' in query:
        #     # ec.capture(0,"test","img.jpg")
        #     camera_port = 0
        #     camera = cv2.VideoCapture(camera_port)
        #     time.sleep(0.1)
        #     return_value, image = camera.read()
        #     cv2.imwrite("opencv.jpg", image)
        #     del(camera)  # so that others can use the camera as soon as possible
        # Imports the Google Cloud client library

        # Instantiates a client
        elif 'who are you' in query:
            speak("I'm Jarvis, I'm your personal assistant.")

        elif 'translate'in query:
        
            translate_client = translate.Client()
            speak("what's to be translated?")
        # The text to translate
            text = takeCommand()
        # The target language
            target = 'ta'

        # Translates some text into Russian
            translation = translate_client.translate(
                text,
                target_language=target)

            # print(u'Text: {}'.format(text))
            print(u'Translation: {}'.format(translation['translatedText']))
            engine.say(translation)
            engine.runAndWait()
