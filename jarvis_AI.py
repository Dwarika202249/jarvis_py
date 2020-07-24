import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import random
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")
    # time.sleep(1)
    speak("I am Jarvis, Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Dwarika said: {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            search = query.split(" ")[1]
            url = f"https://www.youtube.com/results?search_query={search}"
            webbrowser.get().open(url)

        elif 'google' in query:
            search = query.split(" ")[1]
            webbrowser.get().open(f"https://google.com/search?q={search}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\Dwarika Chand\\DJ SONGS'
            songs = os.listdir(music_dir)

            os.startfile(os.path.join(
                music_dir, songs[random.randint(0, len(songs))]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("fine ,sir! what about you?")

        elif 'good' in query:
            speak("great sir!")

        elif 'not good' in query:
            speak("you should take rest, sir!")

        elif 'favourite movie' in query:
            speak("All marvel movies like iron man, avengers, thor")

        elif 'favourite actor' in query:
            speak("your {query} is shahrukh khan")

        elif 'girlfriend' in query:
            speak("all are traitors, i have no allow to speak about it.")

        elif 'favourite subject' in query:
            speak("maths but recently python")

        elif 'brother and sister' in query:
            speak("Dwarika have two younger brothers and one little sister.")

        elif 'friends' in query:
            speak(
                "i think you want to know friends name that is pintu, kundan, naveen, pawan, shyam and so on.")

        elif 'birthday' in query:
            x = datetime.datetime.now().strftime("%m-%d")
            if x == "06-01":
                speak("Happy birthday sir!")
            else:
                speak("Today is not your birthday sir!")

        elif 'arti' in query:
            speak(
                "sir, she is your very close friend and i think she is your crush defenitely. lol")

        elif 'divya' in query:
            speak("she is your first girlfriend and first love. but unfortunately she betrayed you. sad moment.But now she is in touch with you.")

        elif 'sangeeta' in query:
            speak(
                f"{query} is very humble, sweet and very cute girl thats why she is the love of your's sir.")

        elif 'quit' in query:
            speak("Happy to serve you sir!")
            exit()
