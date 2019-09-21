import speech_recognition as sr

from googlesearch import *

import webbrowser as wb

import random

import keyboard as kb

import time as t

import subprocess

import threading

import os

from Voice import captureVoice

def nameChange ():
    print("Yui: Okay, what would you like me to call you?")
    global name
    name = captureVoice()
    return "Alright, you will be known as " + name + " from now on!"



def findMe (voice):
    query = voice
    print("Loading...\n")

    for url in search(query, tld="ca", num=1, stop = 1, pause = 2):
        wb.open("https://google.ca/search?q=%s" % query)

    return "Opening search engine in browser..."



def youtube (voice):
    print("Loading...\n")

    wb.open("https://www.youtube.com/results?search_query=" % voice)
    print("Yui: Okay, here is what I found:\n")
    
    return "Opening results on YouTube..."



def learnMore (voice):
    print("Loading...\n")

    wb.open("https://en.wikipedia.org/wiki/%s" % voice)
    print("Yui: Okay, here is what I found:\n")
    
    return "Opening results in browser..."



def ateBall ():
    
    print("Yui: What question would you like to ask?")
    question = captureVoice()
    choice = random.randrange(1, 6, 1)
    
    if (choice == 1):
        return "No"
    
    elif (choice == 2):
        return "Yes"
    
    elif (choice == 3):
        return "Maybe..."
    
    elif (choice == 4):
        return "For sure!"

    elif (choice == 5):
        return "Never!"

    elif (choice == 5):
        return "Ask again"



def openApp(app):
 
    if (app == "audio converter"):
        subprocess.Popen("C:\Program Files (x86)\Anvsoft\Any Audio Converter\AACFree.exe")
        return "Opening AAC..."

    elif (app == "steam"):
        subprocess.Popen("C:\Program Files (x86)\Steam\Steam.exe")
        return "Opening Steam..."

    elif (app == "Battlenet"):
        subprocess.Popen("C:\Program Files (x86)\Blizzard App\Battle.net.exe")
        return "Opening Battle.Net"

    elif (app == "photoshop"):
        subprocess.Popen("C:\Program Files\Adobe\Adobe Photoshop CC 2015\Photoshop.exe")
        return "Opening Photoshop..."
    
    elif (app == "OBS"):
        subprocess.Popen("C:\Program Files (x86)\obs-studio\bin\64bit\obs64.exe")
        return "Opening OBS..."

    elif (app == "league"):
        subprocess.Popen("D:\LOL\LeagueClient.exe")
        return "Opening League of Legends..."

    else:
        return "Sorry, I can't find that app"



def song():
    os.startfile("D:\\Jimmy's Stuff\\Music\\SAO\\[ASL] Yui (CV Itou Kanae) - Sword Art Online Bonus Disc 5 [FLAC]\\01 I know ai.flac")
    return "Enjoy the song!"



def choose (choice):
    if (choice == "1" ):
        return 0
    
    else:
        if (choice == "one"):
            return 0
        
        elif (choice == "two"):
            return 1
        
        elif (choice == "three"):
            return 2
        
        elif (choice == "four"):
            return 3

        elif (choice == "five"):
            return 4
