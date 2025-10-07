import time
import pyautogui
import pydirectinput as p
import keyboard

# pip install Pillow
# pip install opencv-python

SLEEP_SHORT = 0.2
SLEEP_MEDIUM = 0.5
SLEEP_LONG = 1.0

nickname = input("nickname:>> ")

time.sleep(2)


def lava(file: str) -> bool:

    time.sleep(SLEEP_MEDIUM)
    try:
        pn = pyautogui.locateOnScreen(file, confidence=0.67)
        if pn is not None:
            p.keyDown("s")
            time.sleep(0.6)
            p.keyUp("s")
            time.sleep(SLEEP_MEDIUM)

            pyautogui.typewrite("2")
            time.sleep(SLEEP_SHORT)

            pyautogui.rightClick()
            time.sleep(SLEEP_SHORT)
            pyautogui.rightClick()

            pyautogui.typewrite("1")
            return False
    except Exception:
        pass
    return True


def mine_block():
    p.mouseDown()
    time.sleep(1.2)
    p.mouseUp()


def walk_forward():
    p.keyDown("w")
    time.sleep(0.3)
    p.keyUp("w")


def chat(file: str) -> bool:
    try:
        found = pyautogui.locateOnScreen(file, confidence=0.8)
        if found is not None:
            pyautogui.typewrite(["enter"])
            time.sleep(SLEEP_LONG)
            pyautogui.typewrite("ok", 0.2)
            pyautogui.typewrite(["enter"])
            pyautogui.typewrite(["esc"])
            return False
    except Exception:
        pass
    return True


def end_bot():
    pyautogui.typewrite(["enter"])
    time.sleep(SLEEP_LONG)

    keyboard.write(f"/tp {nickname}")
    time.sleep(SLEEP_SHORT)
    pyautogui.typewrite(["enter"])
    time.sleep(SLEEP_LONG)

    for i in range(1, 10):
        pyautogui.typewrite(str(i))
        time.sleep(SLEEP_SHORT)
        pyautogui.hotkey("ctrl", "q")
        time.sleep(SLEEP_SHORT)

    pyautogui.typewrite(["enter"])
    time.sleep(SLEEP_SHORT)
    pyautogui.typewrite("end", 0.2)
    pyautogui.typewrite(["enter"])
    time.sleep(SLEEP_SHORT)
    pyautogui.typewrite(["esc"])



def main():
    while True:
        if not chat("start.png"):
            break
        time.sleep(SLEEP_SHORT)

    time.sleep(SLEEP_LONG)

    while True:
        mine_block()
        if not lava("lava.png"):
            break
        walk_forward()

    end_bot()


if __name__ == "__main__":
    main()

