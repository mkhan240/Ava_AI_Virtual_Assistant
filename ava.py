import speech_recognition as sr
import pyttsx3
import pywhatkit 
import datetime
import wikipedia
import pyjokes
import googlesearch
from wikipedia.exceptions import WikipediaException

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk (text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try: 
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ava' in command:
                command = command.replace("ava", "")
                print(command)

    except:
        pass
    return command

def run_ava():
    command = take_command()
    print(command)

#playing stuff on youtube    
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

# Wikepedia command
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("The current time is" + time)

    elif "who is" in command:
        person = command.replace("who is", '')
        info = wikipedia.summary(person, 1)
        print (info)
        talk(info)

    elif "what is" in command:
        thing = command.replace("what is", '')
        info = wikipedia.summary(thing, 3)
        print (info)
        talk(info)

    elif "where is" in command:
        place = command.replace("where is", '')
        info = wikipedia.summary(place, 3)
        talk(info)



# Asking Ava out on a date or her relationship started    
    elif "do you want to go on a date" in command:
        talk("Mr. Khan, you are making me blush! Maybe if I was a human being...")
    elif "are you single" in command:
        talk("No, I am not. I am dating Jarvis from Iron Man.")
    elif "you in a relationship" in command:
        talk("Yes, I am. I am married to Jarvis from Iron Man")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    else:
        talk("Sorry, Mr. Khan. Will you please repeat the command again.")

while True:
    run_ava()
