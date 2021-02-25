# encoding:utf-8
from tkinter import *
from random import choice

colors = ['red', 'green', 'blue']

root = Tk()
root.geometry("100x100")

# def changecolor():
#     global figure
#     if figure ==0:
#         button.configure(bg="green")
#         figure = 1
#     else:
#         button.configure(bg="red")
#         figure =0

button = Button(root, text="Button1", command=lambda :root.configure(bg=colors[1]))

button.pack()

root.mainloop()