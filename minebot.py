import pydirectinput as p
import time
import pyautogui
#pip install Pillow
#pip install opencv-python
time.sleep(5)
start = True
def lava(file):
    time.sleep(0.5)
    try:
        pn = pyautogui.locateOnScreen(file, confidence=0.67)
        if pn != None:
            p.keyDown('s')
            time.sleep(0.6)
            p.keyUp('s')
            time.sleep(0.5)
            pyautogui.typewrite(['2'])
            time.sleep(0.1)
            pyautogui.rightClick()
            time.sleep(0.1)
            pyautogui.rightClick()
            pyautogui.typewrite(['1'])
            return True
    except:
        return False
def mineblock():
    p.mouseDown()
    time.sleep(1.2)
    p.mouseUp()
def walkforward():
    p.keyDown('w')
    time.sleep(0.2)
    p.keyUp('w')
            
    

while start:
    mineblock()
    found = lava('lava.png')
    if found:
        start = False
        break
    walkforward()
    
