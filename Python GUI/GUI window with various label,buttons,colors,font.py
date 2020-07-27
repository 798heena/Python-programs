#Python program to demontrate complete details of GUI window

from tkinter import *
gui = Tk()
def hello():
    c = a.get()
    guil3 = Label(text=c, fg='red', bg='yellow', font=10).pack()
def delete():
    guil4 = Label(text='Delete', fg='red', bg='yellow', font=10).pack()
a = StringVar()
gui.title("Aliyas Shaik Button Program")
gui.geometry("500x500+100+100")
guil1 = Label(text='Label One', fg='red', bg='yellow', font=10).pack()
button1 = Button(text='Enter', fg='red', bg='yellow', command=hello, font=10).pack()
button2 = Button(text='Delete', fg='red', bg='yellow', command=delete, font=10).pack()
# Place method places label @ specified place within the window
text = Entry(textvariable=a).pack()
gui.mainloop()