import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import subprocess
import pyjokes
#import pyAudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Deepak!")

    elif hour>=12 and hour<16:
        speak("Good afternoon Deepak!")   

    else:
        speak("Good Evening Deepak!")  

    speak("mai aapka personal assistant hoon sir")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('deshdeepak0099@gmail.com', 'deepak9918960993')
    server.sendmail('deshdeepak0099@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'my name ' in query:
            speak("Sir your name is Deepak")
        elif 'who i am' in query:
            speak("If you talk then definately your human.")
        elif "why you came to world" in query:
            speak("Thanks to Deepak sir. further It's a secret")
        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")
        elif "who are you" in query:
            speak("I am your virtual assistant created by Deepak")
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "will you be my gf" in query or "will you be my bf" in query:   
            speak("I'm not sure about, may be you should give me some time")
        elif "how are you" in query:
            speak("I'm fine sir,  how are you sir?")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "i love you" in query:
            speak("It's hard to understand")
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Gaurav.")
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        

        elif 'email to Deepak' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "deshdeepak0099@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Deepak bhai. I am not able to send this email")
        elif 'exit' in query:
            speak("Thanks for giving me your time sir")
            exit()
         
        
 
        
