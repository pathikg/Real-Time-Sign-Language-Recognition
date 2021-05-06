import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
from hand_detection import capture

import matplotlib
matplotlib.use('Agg')


def show_frame(frame):
    frame.tkraise()


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open(
            r"skinMask 200\images\bg_img.jpeg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


window = tkinter.Tk()

window.geometry('640x480')
window.title("Sign Language Recognition")
window.resizable(width=False, height=False)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tkinter.Frame(window)
frame2 = tkinter.Frame(window, bg='#0F0C08')
frame3 = tkinter.Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')


# --------------------------------------------Main Screen----------------------------------------
# load = Image.open("bg_img.jpeg")
# render = ImageTk.PhotoImage(load)

# img = Label(frame1, image=render)
# img.image = render
# img.place(x=0, y=0)

e = Example(frame1)
e.pack(fill=BOTH, expand=YES)

label = tkinter.Label(
    frame1, text="Sign Language Recognition", font=("Arial Bold", 30))
label.place(relx=0.5, rely=0.08, anchor='n')


button1 = tkinter.Button(frame1, text="Start", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: capture())
button1.place(x=430, y=175)

button2 = tkinter.Button(frame1, text="About", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame2))
button2.place(x=430, y=250)

button3 = tkinter.Button(frame1, text="Contact Us", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame3))
button3.place(x=430, y=325)

button4 = tkinter.Button(frame1, text="Exit", font=(
    "Arial Bold", 12), height=2, width=15, command=window.destroy)
button4.place(x=430, y=400)


# --------------------------------------------About US----------------------------------------

# e = Example(frame2)
# e.pack(fill=BOTH, expand=YES)


load = Image.open(
    r"skinMask 200\images\shinyblack1.jpg")
render = ImageTk.PhotoImage(load)

img = Label(frame2, image=render)
img.image = render
img.place(x=0, y=0)


label = tkinter.Label(frame2, text="About Us", font=("Arial Bold", 30))
label.place(relx=0.5, rely=0.08, anchor='n')

label1 = tkinter.Label(frame2, text="We are making a sign language recognition system \nthat will help to bridge the gap of communication\nbetween Deaf-mutes and normal people.\nThis system works on the Neural Networks which will\nbe able to recognize the Signs in the Sign language\nand will be able to translate that sign into its \ncorresponding word or letter or speech. Furthermore\n this system can be integrated with websites or \napplications through which users can communicate \nmore effectively and also in future this can be \nused in robots to understand Sign Language and \nrespond to the respective user.\n", bg='#FEFEFE',
                       font=("Arial Bold", 12))
label1.place(relx=0.32, rely=0.364, anchor='n')

button1 = tkinter.Button(frame2, text="Home", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame1))
button1.place(x=450, y=175)

button2 = tkinter.Button(frame2, text="About", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame2))
button2.place(x=450, y=250)

button3 = tkinter.Button(frame2, text="Contact Us", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame3))
button3.place(x=450, y=325)

button4 = tkinter.Button(frame2, text="Exit", font=(
    "Arial Bold", 12), height=2, width=15, command=window.destroy)
button4.place(x=450, y=400)


# --------------------------------------------Contact Us----------------------------------------
frame3.configure(bg='gainsboro')

load = Image.open(
    r"skinMask 200\images\shinyblack1.jpg")
render = ImageTk.PhotoImage(load)

img = Label(frame3, image=render)
img.image = render
img.place(x=0, y=0)

label = tkinter.Label(frame3, text="Contact Details", font=("Arial Bold", 30))
label.place(relx=0.5, rely=0.08, anchor='n')

label1 = tkinter.Label(frame3, text="\nMayank Chopra \n +91 750-649-9595\nmayank.chopra@somaiya.edu\n\nPathik Ghugare \n +91 842-581-7345\npathik.g@somaiya.edu\n", anchor='w',
                       font=("Olivia Bold", 14), bg='grey')
label1.place(relx=0.3, rely=0.35, anchor='n')

button1 = tkinter.Button(frame3, text="Home", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame1))
button1.place(x=430, y=175)

button2 = tkinter.Button(frame3, text="About", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame2))
button2.place(x=430, y=250)

button3 = tkinter.Button(frame3, text="Contact Us", font=(
    "Arial Bold", 12), height=2, width=15, command=lambda: show_frame(frame3))
button3.place(x=430, y=325)

button4 = tkinter.Button(frame3, text="Exit", font=(
    "Arial Bold", 12), height=2, width=15, command=window.destroy)
button4.place(x=430, y=400)
#window.wm_attributes("-transparentcolor", 'grey')

show_frame(frame1)
window.mainloop()
