import time
import threading
import pyautogui
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="t")

moving = False


def mover():
    while True:
        if moving:
            pyautogui.moveTo(1200, 929)
            pyautogui.moveTo(1123, 900)
        time.sleep(0.001)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global moving
        moving = not moving
    if moving and key == TOGGLE_KEY:
        print("Auto mouse mover is on.")
    elif key == TOGGLE_KEY:
        print("Auto mouse mover is off.")


move_thread = threading.Thread(target=mover)
move_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
