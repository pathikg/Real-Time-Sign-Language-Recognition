import tkinter
from tkinter import *
from PIL import Image, ImageTk

import matplotlib
matplotlib.use('Agg')


def show_frame(frame):
    frame.tkraise()


window = tkinter.Tk()

window.geometry('640x480')
window.title("GUI")
window.resizable(width=False, height=False)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tkinter.Frame(window)
frame2 = tkinter.Frame(window)
frame3 = tkinter.Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')


# --------------------------------------------Main Screen----------------------------------------
load = Image.open("bg_img.jpeg")
render = ImageTk.PhotoImage(load)

img = Label(frame1, image=render)
img.image = render
img.place(x=0, y=0)

label = tkinter.Label(
    frame1, text="Sign Language Detection", font=("Arial Bold", 35))
label.place(relx=0.5, rely=0.08, anchor='n')


button1 = tkinter.Button(frame1, text="Start", font=(
    "Arial Bold", 8), height=2, width=10, command=lambda: show_frame(frame1))
button1.place(x=500, y=200)

button2 = tkinter.Button(frame1, text="About", font=(
    "Arial Bold", 8), height=2, width=10, command=lambda: show_frame(frame2))
button1.place(x=500, y=250)

button3 = tkinter.Button(frame1, text="Contact Us", font=(
    "Arial Bold", 8), height=2, width=10, command=lambda: show_frame(frame3))
button1.place(x=500, y=300)

button4 = tkinter.Button(frame1, text="Exit", font=(
    "Arial Bold", 8), height=2, width=10, command=window.destroy)
button1.place(x=500, y=350)


# --------------------------------------------About US----------------------------------------
label = tkinter.Label(frame2, text="About Us", font=("Arial Bold", 35))
label.place(relx=0.5, rely=0.08, anchor='n')

label1 = tkinter.Label(frame2, text="Random text \n hsadfhsdihfspdfhsiodfhsdjfhsjdhf\njhdasgofjihgdsgjfhasdjkg", bg='#faf3e0',
                       font=("Arial Bold", 22))
label1.place(relx=0.3, rely=0.35, anchor='n')

button1 = tkinter.Button(frame2, text="Start", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame1))
button1.place(x=625, y=200)

button2 = tkinter.Button(frame2, text="About", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame2))
button2.place(x=625, y=300)

button3 = tkinter.Button(frame2, text="Contact Us", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame3))
button3.place(x=625, y=400)

button4 = tkinter.Button(frame2, text="Exit", font=(
    "Arial Bold", 12), height=2, width=15, command=window.destroy)
button4.place(x=625, y=500)


# --------------------------------------------Contact Us----------------------------------------
frame3.configure(bg='gainsboro')

load = Image.open("bg_img.jpeg")
render = ImageTk.PhotoImage(load)

img = Label(frame3, image=render)
img.image = render
img.place(x=0, y=0)

label = tkinter.Label(frame3, text="Contact Details", font=("Arial Bold", 35))
label.place(relx=0.5, rely=0.08, anchor='n')

label1 = tkinter.Label(frame3, text="    Call us At \n\nMayank Chopra \n +91 750-649-9595\n\nPathik Ghughare \n +91 842-581-7345",
                       font=("Arial Bold", 22), bg='grey')
label1.place(relx=0.3, rely=0.35, anchor='n')

button1 = tkinter.Button(frame3, text="Start", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame1))
button1.place(x=500, y=150)

button2 = tkinter.Button(frame3, text="About", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame2))
button2.place(x=500, y=250)

button3 = tkinter.Button(frame3, text="Contact Us", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame3))
button3.place(x=500, y=350)

button4 = tkinter.Button(frame3, text="Exit", font=(
    "Arial Bold", 12), height=2, width=15, command=window.destroy)
button4.place(x=500, y=150)
#window.wm_attributes("-transparentcolor", 'grey')

show_frame(frame1)
window.mainloop()
