from tkinter import *

root = Tk()
root.title("First GUI program")
root.resizable(width=False, height=False)

clickCount = 0
def clickcommand():
    global clickCount
    clickCount = clickCount + 1
    titlestring = "you clicked " + str(clickCount) + " times"
    title.configure(text=titlestring)


title = Label(root, text="you clicked 0 times", bg="lime", font="TimesNewRoman")
title.pack()
btn = Button(root, text="Click me!", bg="yellow", command=clickcommand)
btn.pack()

root.mainloop()