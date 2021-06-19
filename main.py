import pyautogui
import time

timeQuestion = input("Do you want to set a custom holding time? (y/n): ")

if timeQuestion == "y":
    holdTime = float(input("How long should the mouse buttons be held? (minutes): "))

    time.sleep(10)

    pyautogui.mouseDown(button = "right")
    pyautogui.mouseDown(button = "left")

    time.sleep(holdTime * 60)

    pyautogui.mouseUp(button = "right")
    pyautogui.mouseUp(button = "left")

elif timeQuestion == "n":
    time.sleep(10)

    pyautogui.mouseDown(button = "left")
    pyautogui.mouseDown(button = "right")

else:
    print("Please enter 'y' or 'n'.")
    input("Do you want to set a custom holding time? (y/n): ")