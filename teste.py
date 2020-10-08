import sqlite3 as sql
from newCollaborator.views import return_status
from tkinter import *
from PIL import Image, ImageTk


gui = Tk()

gui.geometry('300x300')
gui.resizable(False, False)
gui.config(bg='#333')

#canvasNext.pack()
path=Image.open(r'static\setaVerde.png').resize((30, 20), Image.ANTIALIAS)
image_r = ImageTk.PhotoImage(path)
canvasNext = Canvas(gui, width=50, height=50, bg='#333', bd=0, highlightthickness=0)
canvasNext.place(x=50, y=50)
canvasNext.create_image(20, 15, image=image_r)

label = Label(gui, image=image_r, bg='#333')
label.pack()





gui.mainloop()
