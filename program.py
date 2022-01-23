# python text to speech library
import pyttsx3                      # pip install pyttsx3
import datetime                     # python library to get current time
import speech_recognition as sr     # pip install SpeechRecognition
# python library to get article summaries
import wikipedia                    # pip install wikipedia
# webbrowers modeul provides an interface to display web based document to users
import webbrowser
import os                           # library to access the local files from os
import random                       # to generate random functions
# library to search on google
# from googlesearch import search     # pip install google-search 
# python library for automating GUI,Used to programmatically control the mouse & keyboard.
import pyautogui                    # pip install PyAutoGUI
# python library to capture the image
# from ecapture import ecapture as ec # pip install ecapture

# importing the voice Assistant Commands from functions module
from functions import *

# Using voice from locally available in windows
# which are used by pyttsx3 to speak out the strings
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# using this voice for thi assistant
engine.setProperty('voice',voices[0].id)

"""
available voice in this machine are:
1. Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
        name=Microsoft David Desktop - English (United States)

2. Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0
        name=Microsoft Hazel Desktop - English (Great Britain)

3. Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
        name=Microsoft Zira Desktop - English (United States)

For this Assistant uses 3rd voice namely Microsoft Zira Desktop - English (United States)
"""

# Function to speak out strings/data 
# using  the pyttsx3 instance
# with voice property of "Microsoft Zira Desktop - English (United States)"
def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except KeyboardInterrupt:
        speak('Byee')
        exit()

# Using google speech_recognition for audio recognization
# and getting string of audio 
# creating instance of 
hear=sr.Recognizer()


def listenAudio():
    """
        take input from user and convert to string
    """
    global hear
    # accessing microphone using pyaudio python library
    with sr.Microphone() as source:
        print("\nListening")              # assistant start listen to the user
        hear.pause_threshold = 1        # seconds of non-speaking audio before a phrase is considered complete
        
        # minimum audio energy to consider for recording is 300
        #  as there is background noice it is increment to cancel the noice
        hear.energy_threshold = 500

        # listening the microphone source data(audio)
        audio = hear.listen(source)

        try:
            # Recognizing the audio
            print("Recognizing")
            # using recognize_google to get text from audio and the language considered is english-india 
            query=hear.recognize_google(audio, language='en-in')
            print('User Said: ',query,"\n")
            return query
        except Exception as e:

            # for internet connection off error terminating the assistant
            if "recognition connection failed" in str(e):
                speak('Turn on your internet connection!')
                speak('try after some time. Bye bye')
                exit()
            print('Say that again please\n')
            return "None"



if __name__ == '__main__':
    
    print("----------------------------------------------------------------------------------")
    print("--- Voice based ☻ Assistant using Python ♥ developed by Mohit, Mihir & Upendra ---")
    print("----------------------------------------------------------------------------------")
    # greeting the user 
    # speak('Hello User!')

    # wishing user according to the current time
    greeting = wish()
    speak(greeting)
    # print(greeting)

    # a variable to keep track of saved images viz. the screenshot and the camaera clicks 
    # to avoid the overridding of the images
    img_count_file = open("image count.txt", "r")
    imgcount=int(img_count_file.read())
    img_count_file.close()

    while True:

        # listening the audio and getting text from that
        # and converting it to lower case to easily match with the appropriate condition 
        query = listenAudio().lower()
        print(query)

        if 'wikipedia' in query or 'tell me about' in query or ('tell' in query and 'about' in query):
            speak('searching wikipedia...')
            res = searchInWikipedia(query)
            if res!='None':
                speak("Accroding to wikipedia ..")
                print(res)
                speak(res)
        
        elif 'open youtube' in query or 'youtube' in query or 'video' in query:
            searchYt(query)

        elif 'open stack overflow' in query:
            openStackoverflow()
            speak('Successfully opened')

        elif 'search google' in query or 'google' in query or 'browse' in query:
            seachGoogle(query)
        
        elif ('.com' in query or '.in' in query) and 'open' in query:
            website=openWesite(query)
            speak(str(website)+" Successfully opened")

        elif 'play music' in query or 'song' in query:
            playMusic()

        elif 'open code' in query or 'court' in query:
            openVSCode()

        elif 'screenshot' in query or 'snapshot' in query:
            snapScreen(imgcount)
            imgcount = imgcount + 1

        elif "click" in query or "camera" in query or "take a photo" in query:
            try:
                speak("say cheeze!")
                clickPic(imgcount)
            except Exception as e:
                continue

            imgcount= imgcount+1   

        elif 'quit' in query or 'exit' in query or 'bye' in query:
            break

        else:
            speak("Sorry, I didn't recognize this command!!")
    
    
    # writing into the image count.txt file the current name of the screenshot and image clicked
    # to avaoid over writing
    img_count_file = open("image count.txt", "w")
    img_count_file.write(str(imgcount))
    img_count_file.close()
    speak("Pleasure having you. Thank you for having me. Byee ")