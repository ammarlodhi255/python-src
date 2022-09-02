import datetime
import pyttsx3 
import speech_recognition as sr
import wikipedia as wiki
import webbrowser
import os
import random
import smtplib as smt

engine = pyttsx3.init('sapi5') # Microsoft API for Speech Recognition
voices = engine.getProperty('voices') #Returns all the available voices (can you add your custom ones?)
engine.setProperty('voice', voices[0].id) #Setting the preferred agent voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet_me(name):
    greet_str = f"{get_day_greeting()}, {name}"
    speak(greet_str)

def get_day_greeting():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        return "Good Morning"
    elif hour >= 12 and hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

def voice_to_str():
    recognizer = sr.Recognizer()
    with sr.Microphone() as microphone_source:
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(microphone_source, duration = 3)
        print("I'm Listening..")
        speak("I'm Listening..")
        audio = recognizer.listen(microphone_source)

        try:
            print('Processing...')
            speak('Please wait, while I process your request')
            query = recognizer.recognize_google(audio, language='en-in')
        except Exception as ex:
            speak(" I didn't hear you please try saying that again loudly after i say i'm listening")
            return "None"
    return query

def get_voicemail():
    speak('what should I say? Please say your message after I say I\'m listening')
    content = voice_to_str()
    while content == 'None':
        content = voice_to_str()
    return content

def send_mail(mail, content):
    try:
        server = smt.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login('ammarlodhi670@gmail.com', 'kevinowens')
        server.send('ammarlodhi670@gmail.com', mail, content)
        server.close()
    except:
        speak('I cannot reach the specified email at the moment')
        return False
    return True


if __name__ == "__main__":
    greet_me("Sir Amaar")

    while True:
        response = 'no'
        query = str()
        
        while response == 'no':
            query = voice_to_str()
            if query == "None": continue
            speak('You spoke ' + query)
            speak('Say yes if this is correct otherwise say no.. after i say "I\'m Listening\'')
            response = (voice_to_str()).lower()
            while response != 'no' and response != 'yes': 
                response = voice_to_str()

        query = query.lower()
        print(f"Your query is {query}")

        if 'wikipedia' in query:
            print('Searching...')
            speak("Searching wikipedia...")
            results = wiki.summary(query.replace('wikipedia', ''), sentences=2)
            speak('According to wikipedia..')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')
            speak('Youtube has been opened')

        elif 'open google' in query:
            webbrowser.open('http://www.google.com')
            speak('Google has been opened')

        elif 'open facebook' in query:
            webbrowser.open('http://www.facebook.com')
            speak('Facebook has been opened')

        elif 'open stack overflow' in query:
            webbrowser.open('http://www.stackoverflow.com')
            speak('Stack Overflow has been opened')

        elif 'play music' in query:
            music_dir = "D:/Media/Tracks"
            list_of_songs = os.listdir(music_dir)
            rand_selected_song = random.choice(list_of_songs)
            os.startfile(os.path.join(music_dir, rand_selected_song))

        elif 'the time' in query:
            time_str = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir the time is {time_str}')

        # elif 'email to' in query:
        #     name = query[query.find('to ') + 3 :]
        #     # By the way you can import all your contacts from gmail
        #     mail = f'{name}.bscsf19@iba-suk.edu.pk'
        #     content = get_voicemail()
        #     send_mail(mail, content)


        speak('Do you need my further assistance? Say yes, otherwise say no after I say I\'m Listening.')
        res = str()
        while res != 'no' and res != 'yes':
            res = (voice_to_str()).lower()

        if res == 'no':
            bye_str = f'Have a {get_day_greeting()} sir'
            print(bye_str)
            speak(bye_str)
            break