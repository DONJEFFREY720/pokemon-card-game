# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:06:01 2023

@author: Don Jeffrey
"""
from tkinter import*

import random

from PIL import ImageTk , Image

root=Tk()
root.title("Pokimon Game") 
root.geometry("600x400")
root.configure(bg="gold")

##img= ImageTk.PhotoImage(Image.open("button.jpg"))

card1 = ImageTk.PhotoImage(Image.open("card10.jpg"))
card2 = ImageTk.PhotoImage(Image.open("card1.jpg"))
card3 = ImageTk.PhotoImage(Image.open("card2.jpg"))
card4 = ImageTk.PhotoImage(Image.open("card3.jpg"))
card5 = ImageTk.PhotoImage(Image.open("card4.jpg"))
card6 = ImageTk.PhotoImage(Image.open("card5.jpg"))
card7 = ImageTk.PhotoImage(Image.open("card6.jpg"))
card8 = ImageTk.PhotoImage(Image.open("card7.jpg"))
card9 = ImageTk.PhotoImage(Image.open("card8.jpg"))
card10 = ImageTk.PhotoImage(Image.open("card9.jpg"))
card11 = ImageTk.PhotoImage(Image.open("card11.jpg"))
card12 = ImageTk.PhotoImage(Image.open("card12.jpg"))

Player1 = Label(root,text="PLAYER 1",bg="royalblue",fg="white")
Player1.place(relx=0.1,rely=0.3,anchor=CENTER)

Player2 = Label(root,text="PLAYER 2",bg="royalblue",fg="white")
Player2.place(relx=0.9,rely=0.3,anchor=CENTER)

Player1_score = Label(root,text="",bg="royalblue",fg="white")
Player1_score.place(relx=0.1,rely=0.4,anchor=CENTER)

Player2_score = Label(root,text="",bg="royalblue",fg="white")
Player2_score.place(relx=0.9,rely=0.4,anchor=CENTER)

random_dice = Label(root,bg="chocolate",fg="white")
random_dice.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
