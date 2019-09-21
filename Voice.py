import speech_recognition as sr

import time as t

name = "Jimmy"

# obtain audio from the microphone
def captureVoice ():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            message = r.recognize_google(audio)
            
            if (message == "access code Heathcliff password administrator"):
                print("Access code: ********** \nPassword: *************\n")
                return "!@#$%"
            
            elif ("UE" in message):
                message = message.replace("UE", "yui")
                print(name + ": " + message + "\n")
                return message

            elif ("you we" in message):
                message = message.replace("you we", "yui")
                print(name + ": " + message + "\n")
                return message
            
            elif ("you eat" in message):
                message = message.replace("you eat", "yui")
                print(name + ": " + message + "\n")
                return message

            elif ("Yuri" in message):
                message = message.replace("Yuri", "yui")
                print(name + ": " + message + "\n")
                return message

            elif ("to me" in message):
                message = message.replace("to me", "yui")
                print(name + ": " + message + "\n")
                return message

            else:
                print(name + ": " + message + "\n")
                return message

            
        except sr.UnknownValueError:
            t.sleep(0.001)
        
        except sr.RequestError as e:
            print("Could not establish connection to Google Speech Recognition service; {0}".format(e))



def delete (voice):
    end = len(voice)
    start = voice.find("listen yui")
    message = voice[start:end]
    
    return message

