import pydirectinput as p
import time
import pyautogui
import keyboard
#version 0.1 
#pip install Pillow
#pip install opencv-python
def press(key):
    keyboard.press_and_release(key)
def removeblock(sleep):
    p.mouseDown()
    time.sleep(float(sleep))
    p.mouseUp()
def walk(key, sleep, shift=False):
    if shift:
        p.keyDown('shift')
    p.keyDown(str(key))
    time.sleep(float(sleep))
    p.keyUp(str(key))
    if shift:
        p.keyUp('shift')
def screen(file, conf):
    try:
        pn = pyautogui.locateOnScreen(file, confidence=float(conf))
        if pn != None:
            return True
    except:
        return False
def click(mod, x=None, y=None):
    if mod == "l":
        if x != None and y != None:
            p.mouseDown(int(x), int(y), button="left")
            time.sleep(0.1)
            p.mouseUp(button="left")
        else:
            p.mouseDown(button="left")
            time.sleep(0.1)
            p.mouseUp(button="left")
    elif mod == "r":
        if x != None and y != None:
            p.mouseDown(int(x), int(y), button="right")
            time.sleep(0.1)
            p.mouseUp(button="right")
        else:
            p.mouseDown(button="right")
            time.sleep(0.1)
            p.mouseUp(button="right")
def find(image, conf):
    try:
        image1 = pyautogui.locateOnScreen(image, confidence=float(conf))
        buttonpoint = pyautogui.center(image1)
        buttonx, buttony = buttonpoint
        return buttonx, buttony
    except:
        return False
def chat(key, msg):
    if key == "r":
        try:
            found = pyautogui.locateOnScreen(msg, confidence=0.8)
            if found != None:
                return True
        except:
            return False
    if key == "w":
        pyautogui.typewrite("t")
        time.sleep(1)
        keyboard.write(str(msg))
        pyautogui.typewrite(["enter"])
def jump(sleep):
    p.keyDown("space")
    time.sleep(float(sleep))
    p.keyUp("space")
def setblock():
    p.mouseDown(button="right")
    time.sleep(0.1)
    p.mouseUp(button="right")
def select(num):
    pyautogui.typewrite(str(num))
def drop(mod=""):
    if mod == None:
        pyautogui.typewrite(["q"])
    elif mod == "all":
        pyautogui.hotkey("ctrl", "q")
