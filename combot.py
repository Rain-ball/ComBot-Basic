import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import os
#from bs4 import BeautifulSoup
engine = pyttsx3.init()
voices = engine.getProperty("voices")
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
wbsearch = wb.get()
x = 2

engine.setProperty("voice", voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Hello, I am ComBot, nice to meet you.")
speak("Hello, I am ComBot, mice to meet you.")
print("How may I help you?")
speak("How may I help you?")
with sr.Microphone() as source:
    while x == 2:
        print("Listening...")
        audio = r3.listen(source)
        try:
            print("You said : " + r1.recognize_google(audio))
            if r1.recognize_google(audio) == "search YouTube":
                speak("Search query please")
                print("Listening...")
                audio = r1.listen(source)
                print("You said : " + r1.recognize_google(audio))
                get = r1.recognize_google(audio)
                url = "https://www.youtube.com/results?search_query="
                wbsearch.open(url + get)
            if r1.recognize_google(audio) == "open oneline compiler":
                get = "https://onlinegdb.com"
                wbsearch.open_new(get)
            if r1.recognize_google(audio) == "open Notepad":
                os.startfile("notepad.exe")
            if r1.recognize_google(audio) == "open 1 note":
                os.startfile("onenote.exe")
            if r1.recognize_google(audio) == "open Microsoft paint":
                os.startfile("mspaint.exe")
            if r1.recognize_google(audio) == "open code editor":
                os.startfile("notepad++.exe")
            if r1.recognize_google(audio) == "exit":
                input("Press enter to exit.")
                break
        except sr.UnknownValueError:
            print("Error")
        except sr.RequestError:
            print("Failed Error")
