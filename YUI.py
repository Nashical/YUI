#!/usr/bin/env python3

import speech_recognition as sr

from googlesearch import *

import webbrowser as wb

import random

import keyboard as kb

import time as t

from Voice import *

from Choices import options

from plyer import notification



def startYUI():
# ----------------------------------------------------\ Global Vars /--------------------------------------------------- #

    name = "Jimmy"

# --------------------------------------------------------\ Main /------------------------------------------------------ #

    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)


    print("Hello " + name + ", I am Sword Art Online's Mental Health Companion Program Yui-MHCP001, or just Yui for short!")
          
    #name = captureVoice()

    print("How may I be of assistance to you today?\n")

    voice = captureVoice()

    while(True):

        if (voice == None):
            voice = captureVoice()

        elif (voice == "stop"):
            break
        
        elif ("listen yui" in voice):
            voice = delete(voice)
            voice = voice.replace("listen yui ", "")
            message = voice.lower()

            if (message == "logout"):
                print("Logging out " + name + "...")
                break
                
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            reply = options(message) + "\n"
            print("Yui: " + reply)

            notification.notify(
                title = 'Yui-MHCP001',
                message = reply,
                app_icon = "D:\\Jimmy's Stuff\\Projects\\AI\\YUI\\Yui.ico",  # e.g. 'C:\\icon_32x32.ico'
                timeout = 5,  # seconds
            )
            
            voice = captureVoice()

        else:
            voice = captureVoice()
