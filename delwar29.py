import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import wolframalpha


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)     
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('Who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info) 
    elif'show me covid info' in command:
        webbrowser.open("http://dashboard.dghs.gov.bd/webportal/pages/covid19.php")
    elif'open youtube' in command:
        webbrowser.open("youtube.com")
    elif'open google' in command:
        webbrowser.open("google.com")
    elif'open facebook' in command:
        webbrowser.open("facebook.com")
    elif'open code blocks' in command:
        webbrowser.open("C:\Program Files\CodeBlocks\codeblocks.exe")
    elif 'who are you' in command:
        talk('My name is jarvis and I am a machine, Without instruction I cannot do anything')
    elif 'what can you do' in command:
        talk('I can calculate, I can play music on youtube, I can convert currency, I able to open various broweser like Google, Facebook, youtube , I can share jokes, I can search on wikipedia, I can tell you about update temperature and update time')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    

    elif 'calculate' in command:
        app_id = ("L7H765-5GLHPGHGQE")
        client = wolframalpha.Client(app_id)
        res = client.query(command)
        answer = next(res.results).text
        talk(f"your answer is {answer}")
        print(f"your answer is {answer}")

    elif 'temperature' in command:
        app_id = ("L7H765-5GLHPGHGQE")
        client = wolframalpha.Client(app_id)
        res = client.query(command)
        answer = next(res.results).text
        talk(f"your answer is {answer}")
        print(f"your answer is {answer}")

    elif 'convert currency' in command:
        app_id = ("L7H765-5GLHPGHGQE")
        client = wolframalpha.Client(app_id)
        res = client.query(command)
        answer = next(res.results).text
        talk(f"your answer is {answer}")
        print(f"your answer is {answer}")

    else:
        talk('Please say the command again.')

while True:
    run_jarvis()

