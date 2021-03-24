import subprocess
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import os


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        return "None"
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    #elif 'exit' in command:
    #    talk("Thanks for giving me your time")
    #    exit()
    elif "weather" in command:

        # Google Open weather website
        # to get API of Open weather
        api_key = "Api key"
        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        talk(" City name ")
        print("City name : ")
        city_name = take_command()
        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        response = requests.get(complete_url)
        x = response.json()



    elif "off" in command or "sign out" in command:
        talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
        subprocess.call(["shutdown", "/l"])

    elif "open stackoverflow" in command:
        webbrowser.open_new_tab("https://stackoverflow.com/login")
        talk("Here is stackoverflow")

    elif 'open google' in command:
        webbrowser.open_new_tab("https://www.google.com")
        talk("Google chrome is open now")
        #time.sleep(5)
    elif 'open youtube' in command:
        webbrowser.open_new_tab("https://www.youtube.com")
        talk("youtube is open now")

    else:
        talk('Please say the command again.')

while True:
    run_alexa()


