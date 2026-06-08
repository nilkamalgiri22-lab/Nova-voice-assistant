import speech_recognition as sr
import webbrowser
# import pyttsx3
from gtts import gTTS
import pygame
import os
from pydub import AudioSegment
import musiclibrary
from client import aiProcess
from news import fetchNews



recognizer = sr.Recognizer()

# def speak(text):
    # engine = pyttsx3.init()
    # engine.say(text)
    # engine.runAndWait()


def speak(text, speed=1.5):   # 1.2 = Alexa-like speed, tune this!
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save("response.mp3")
    
    # Load and change speed
    audio = AudioSegment.from_mp3("response.mp3")
    fast_audio = audio.speedup(playback_speed=speed)
    fast_audio.export("response_fast.mp3", format="mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("response_fast.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("response.mp3")
    os.remove("response_fast.mp3")


def process_command(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif c.lower().startswith("play"):
        song =c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "tell news" in c.lower():
        speak("Fetching top news headlines")
        titles = fetchNews()
        if titles:
            speak(f"Here are the top {len(titles)} headlines")
            for i, title in enumerate(titles, start=1):
                speak(f"News {i}: {title}")
        else:
            speak("Sorry, I could not fetch the news right now.")
    else:
       # Send the command to Gemini
        print("Thinking...")
        output = aiProcess(c)
        print("nova:", output)
        speak(output)


if __name__ == "__main__":
    speak("Initializing nova...")

    # Listen for the wake word "nova"
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=5)

            command = r.recognize_google(audio)
            print("You said: " + command)

            if command.lower() == "nova":
                speak("Yes")

                # Listen for actual command
                with sr.Microphone() as source:
                    print("nova active...")
                    audio = r.listen(source)
                command = r.recognize_google(audio)
                
                process_command(command)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Google Speech Recognition error; {0}".format(e))
        except Exception as e:
            # Catch-all for any other weird errors so your loop doesn't crash
            print(f"An error occurred: {e}")