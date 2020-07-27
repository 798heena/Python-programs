#Python program to demonstrate label,font,color

from tkinter import *
gui = Tk()
gui.title("Aliyas Shaik Button Program")
gui.geometry("500x500+100+100")
guil1 = Label (text='Label One',fg='red',bg='yellow').pack()
button1 = Button(text='Enter',fg='red',bg='yellow').pack()
#Place method places label @ specified place within the window
gui.mainloop()