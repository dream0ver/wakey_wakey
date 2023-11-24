from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key,Controller as KBController
import tkinter as tk
import time

mouse = MouseController()
kb = KBController()
flag = True
moveBy = 10
root = tk.Tk()
screen_width_half = root.winfo_screenwidth()/2
screen_height_half = root.winfo_screenheight()/2

print("wakey wakey service started running. Press CTRL + C to exit.")

mouse.position = (screen_width_half , screen_height_half )

while True:
	if flag:
		mouse.move(moveBy ,-moveBy)
	else:
		mouse.move(-moveBy ,moveBy)
	kb.press(Key.scroll_lock)
	kb.release(Key.scroll_lock)
	flag = not flag
	time.sleep(5)