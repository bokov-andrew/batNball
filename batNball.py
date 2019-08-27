import tkinter
import time
from tkinter import messagebox

canvasWidth=750
canvasHeight=500
window=tkinter.Tk()
canvas=tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg='dodgerblue4')
canvas.pack()
bat=canvas.create_rectangle(0,0,40,10,fill='dark turquoise')
ball=canvas.create_oval(0,0,10,10,fill='deep pink')
windowOpen=True
def main_loop():
    while windowOpen==True:
        move_bat()
        move_ball()
        window.update()
        time.sleep(0.02)
        if windowOpen==True:
            check_game_over()
leftPressed = 0
rightPressed = 0

def on_key_press(event):
    global leftPressed, rightPressed
    if event.keysym == 'Left':
        leftPressed = 1
    elif event.keysym == 'Right':
        rightPressed = 1
        
def on_key_release(event):
    global leftPressed, rightPressed
    if event.keysym == 'Left':
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0

batSpeed = 6

def move_bat():
    batMove = batSpeed*rightPressed-batSpeed*leftPressed
    (batLeft,batTop,batRight,batBottom)=canvas.coords(bat)
    if (batLeft > 0 or batMove > 0)and(batRight < canvasWidth or batMove < 0):
        canvas.move(bat, batMove, 0)
        
def move_ball():
    pass

def check_game_over():
    pass

window.bind("<KeyPress>",on_key_press)
window.bind("<KeyRelease>",on_key_release)
main_loop()