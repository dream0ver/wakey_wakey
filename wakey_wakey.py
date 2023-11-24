from pynput.mouse import Controller
import tkinter as tk
import time

mouse = Controller()
offsetY = -1
offsetX = 1
moveBy = 10
root = tk.Tk()
screen_width_half = root.winfo_screenwidth()/2
screen_height_half = root.winfo_screenheight()/2

print("wakey wakey service started running. Press CTRL + C to exit.")

mouse.position = (screen_width_half , screen_height_half )

while True:
	mouse.move(offsetX*moveBy ,offsetY*moveBy )
	offsetY  = offsetY *(-1)
	offsetX= offsetX *(-1)
	time.sleep(5)