import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

from secret import cloud_cred

GOOGLE_CLOUD_SPEECH_CREDENTIALS = cloud_cred

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    # try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        # print('test')
        command = listener.recognize_google_cloud(voice, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
        print('test')
        command = command.lower()
        if 'doncho' in command:
            command = command.replace('doncho', '')
            print(command)
    # except:
    #     pass
    return command

def run_doncho():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command: 
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_doncho()