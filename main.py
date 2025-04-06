import tkinter as tk
import random

from window import Window
from collect import generate_collected

def main():
    #win = Window(800, 600)
    window = tk.Tk()
    
    button = tk.Button(
        text="Click to go walking!",
        width=25,
        height=5,
        bg="black",
        fg="white",
    )
    button.bind("<Button-1>", handle_go_walking)
    button.pack()
    window.mainloop()
    #win.wait_for_close()

def handle_go_walking(event):
    collected = generate_collected()
    greeting = tk.Label(text=f"{collected}")
    greeting.pack()

main()