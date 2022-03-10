import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import subprocess
import wolframalpha
import requests
import json

print('Loading the AI Voice Assistant - Robostoa')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hi, Good Morning!")
        print("Hi, Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Hi, Good Afternoon!")
        print("Hi, Good Afternoon!")
    else:
        speak("Hi ,Good Evening!")
        print("Hi ,Good Evening!")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=3)
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"User said: {statement}\n")

        except Exception as e:
            speak("Excuse me, can you say that again")
            return "None"
        return statement


speak("Loading the AI Voice Assistant Robostoa")
wishMe()


if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "goodbye" in statement or "bye" in statement or "stop" in statement:
            speak('Your AI Voice Assistant Robostoa is shutting down, Good bye!')
            print('your AI Voice Assistant Robostoa is shutting down, Good bye!')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://gmail.com")
            speak("G Mail is open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "7e7c1f0e94a0f88363b4a92203c20f60"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak("Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\nhumidity in percentage is " +
                      str(current_humidiy) +
                      "\ndescription  " +
                      str(weather_description))
                print("Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\nhumidity (in percentage) = " +
                      str(current_humidiy) +
                      "\ndescription = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Robostoa, the best AI Robot you will ever find. For now i am programmed to do tasks like'
                  'opening youtube, google, gmail and stackoverflow, predict forecast and weather in different cities, search in wikipedia'
                  'get top headline news from new york times and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Jorge Eldis")
            print("I was built by Jorge Eldis")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab(
                "https://www.nytimes.com/")
            speak('Here are some headlines from the New York Times')
            time.sleep(6)

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "WKV645-PE6XL6URPQ"
            client = wolframalpha.Client('WKV645-PE6XL6URPQ')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak(
                "Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)