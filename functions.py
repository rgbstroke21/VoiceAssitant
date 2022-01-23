import wikipedia
import webbrowser
import os
import random
import datetime 
import pyautogui
# from ecapture import ecapture as ec

def wish():
    hr=int (datetime.datetime.now().hour)
    res=""
    if hr>=0 and hr<12:
        res="Good Morning!"
    elif hr>=12 and hr<18:
        res="Good Afternoon"
    else:
        res="Good Evening"

    res+="\nHow can i help you?"
    return res

def searchInWikipedia(query):
    
    query = query.replace("wikipedia","")
    query = query.replace("tell","")
    query = query.replace("me","")
    query = query.replace("about","")
    print(query)
    try:
        results=wikipedia.summary(query,sentences=1)

    except Exception as e:
        return "None"
    return results

def searchYt(query):
    URL='https://www.youtube.com/'
    if query=="open youtube":
        webbrowser.open_new_tab(URL)
        return
    query = query.replace("open", "")
    query = query.replace("youtube", "")
    query = query.replace("video", "")
    
    if query!="" or query!=" ":
        URL = URL+'search?q='+query;
    webbrowser.open_new_tab(URL)

def openStackoverflow():
    webbrowser.open_new_tab("https://www.stackoverflow.com")

def seachGoogle(query):
    query = query.replace("open", "")
    query = query.replace("google", "")
    query = query.replace("browse","")
    query = query.replace("search","")
    
    URL='https://www.google.com/'
    if query!="" or query!=" ":
        URL = URL+'search?q='+query;
    webbrowser.open_new_tab(URL)

def openWesite(query):
    query = query.replace("open", "")
    query = query.replace(" ", "")
    if query != "":
        URL='https://www.'+query
        webbrowser.open_new_tab(URL)
        return query

def playMusic():
    music_loc='musics'
    songs=os.listdir(music_loc)
    print(songs)
    os.startfile(os.path.join(music_loc,songs[random.randint(0,len(songs))]))

def openVSCode():
    code_loc=r"C:\Users\mihir\AppData\Local\Programs\Microsoft VS Code\code.exe"
    os.startfile(code_loc)

def snapScreen(i):
    pyautogui.screenshot().save('./images/ss'+str(i)+'.png')

def clickPic(i):
    ec.capture(0, "Jarvis Camera ", "./images/img"+str(i)+".jpg")






