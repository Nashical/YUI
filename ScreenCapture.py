from pynput.keyboard import Key, Controller as KeyboardController

from pynput.mouse import Button, Controller as MouseController

import time as t

from Voice import captureVoice

keyboard = KeyboardController()
mouse = MouseController()

def sendScreen(voice):
    
    if (voice == ""):
        return "Sorry, there wasn't a name specified"
    
    else:
        name = voice.replace(" ", "")
        name = name.lower()
        screenshot(name)
        return "Sent to " + voice



def sendMessage(voice):
    
    if (voice == ""):
        return "Sorry, there wasn't a message specified"
    
    else:
        name = voice.replace(" ", "")
        name = name.lower()
        print("Yui: What would you like to tell them?\n")
        msg = captureVoice()
        sendMsg(name, msg)
        return "Sent to " + voice



def screenshot (name):
    keyboard.press(Key.ctrl_l)
    t.sleep(0.1)
    keyboard.press(Key.shift_l)
    t.sleep(0.1)
    keyboard.press('4')
    t.sleep(0.1)
    keyboard.release('4')
    t.sleep(0.1)
    keyboard.release(Key.shift_l)
    t.sleep(0.1)
    keyboard.release(Key.ctrl_l)
    t.sleep(0.5)
    mouse.press(Button.left)
    t.sleep(0.1)
    mouse.release(Button.left)
    t.sleep(0.5)

    mouse.position = (2537, 225)
    t.sleep(0.1)
    mouse.press(Button.left)
    t.sleep(0.1)
    mouse.release(Button.left)
    t.sleep(0.1)
    mouse.position = (2687, 225)
    t.sleep(0.1)
    mouse.press(Button.left)
    t.sleep(0.1)
    mouse.release(Button.left)
    t.sleep(0.1)
    keyboard.type(name)
    t.sleep(0.5)
    keyboard.press(Key.enter)
    t.sleep(0.1)
    keyboard.release(Key.enter)
    t.sleep(0.1)

    keyboard.press(Key.ctrl_l)
    t.sleep(0.1)
    keyboard.press('v')
    t.sleep(0.1)
    keyboard.release('v')
    t.sleep(0.01)
    keyboard.release(Key.ctrl_l)
    t.sleep(0.5)
    keyboard.press(Key.enter)
    t.sleep(0.1)
    keyboard.release(Key.enter)
    t.sleep(0.1)

def sendMsg(name, message):
    mouse.position = (2537, 225)
    t.sleep(0.1)
    mouse.press(Button.left)
    t.sleep(0.1)
    mouse.release(Button.left)
    t.sleep(0.1)
    mouse.position = (2687, 225)
    t.sleep(0.1)
    mouse.press(Button.left)
    t.sleep(0.1)
    mouse.release(Button.left)
    t.sleep(0.1)
    keyboard.type(name)
    t.sleep(0.5)
    keyboard.press(Key.enter)
    t.sleep(0.1)
    keyboard.release(Key.enter)
    t.sleep(0.1)

    keyboard.type(message)
    t.sleep(1)
    keyboard.press(Key.enter)
    t.sleep(0.1)
    keyboard.release(Key.enter)
    t.sleep(0.1)

    
