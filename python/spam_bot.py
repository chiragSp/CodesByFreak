#ai
import pyautogui
from time import sleep

sleep(5)

f = 0
while True:
	f = f + 1
	m = "You are damm cool (text number = "+ (str(f)) +" )"
	for letter in m:
		pyautogui.typewrite(letter)	
	pyautogui.press("enter")


