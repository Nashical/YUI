from Functions import *

from ScreenCapture import *

import time as t

from Voice import captureVoice

def options(voice):
    
    if (voice == "hello yui"):
        return "Hi, " + name + "! Feel free to ask me for anything!"
        
    elif (voice == "how are you"):
        return "I'm fine!"

    elif (voice == "what is my name"):
        return "From your player info, I belive it is " + name + "!"

    elif (voice == "change my name"):
        return nameChange()

    elif ("google search" in voice):
        voice = voice.replace("google search ", "")
        return findMe(voice)

    elif ("tell me more about" in voice):
        voice = voice.replace("tell me more about ", "")
        return learnMore(voice)

    elif ("open" in voice):
        voice = voice.replace("open ", "")
        return openApp(voice)

    elif ("send this to" in voice):
        voice = voice.replace("send this to ", "")
        return sendScreen(voice)

    elif (voice == "8-ball"):
        return ateBall()

    elif ("find for me on YouTube" in voice):
        voice = voice.replace("find for me on YouTube ", "")
        return youtube(voice)

    elif ("sing for me" in voice):
        return song()

    elif ("send a message to" in voice):
        voice = voice.replace("send a message to ", "")
        return sendMessage(voice)

    elif (voice == "Open console command"):
        print(" ---------------------------------------")
        print("| Cardinal System Administrator Console |")
        print(" ---------------------------------------\n")
        print("Please verify personnel for clearance:\n")
        voice = captureVoice()
    
        if (voice == "!@#$%"):
            t.sleep(1)
            print("Verifying with Cardinal...\n")
            t.sleep(2)
            return "Cardinal System Administrator mode access granted.\nInitializing environment..."

        else:
            return "Unauthorized personnel, I cannot grant you administrator access."

    elif (voice == "goodbye"):
        exit

    elif (voice == ""):
        print("")
    
    else:
        return "Sorry, I didn't quite catch that..."
