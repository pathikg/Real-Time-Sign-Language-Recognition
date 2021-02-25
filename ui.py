import tkinter
from tkinter import *
from PIL import Image, ImageTk

import matplotlib
matplotlib.use('Agg')


window = tkinter.Tk()

window.geometry('900x650')
window.title("GUI")
window.configure(bg = 'gainsboro')
window.resizable(width = False, height = False)

load = Image.open("bg_img.jpeg")
render = ImageTk.PhotoImage(load)

img = Label(window, image=render)
img.image = render
img.place(x=0, y=0)

label =  tkinter.Label(window,text = "Sign Language Detection",font = ("Arial Bold",35))
label.place(relx = 0.5, rely = 0.08, anchor ='n')


button1=tkinter.Button(window, text="Start",font = ("Arial Bold",12),height = 2, width = 15)
button1.place(x=625, y=200)

button2=tkinter.Button(window, text="About",font = ("Arial Bold",12),height = 2, width = 15)
button2.place(x=625, y=300)

button3=tkinter.Button(window, text="Contact Us",font = ("Arial Bold",12),height = 2, width = 15)
button3.place(x=625, y=400)

button4=tkinter.Button(window, text="Exit",font = ("Arial Bold",12),height = 2, width = 15,command = window.destroy)
button4.place(x=625, y=500)


window.mainloop()
