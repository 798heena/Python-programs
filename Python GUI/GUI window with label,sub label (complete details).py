#Python program to demonstrate labels,sub-labels and complete window details

from tkinter import *
gui = Tk()
menu1 = Menu()
listone = Menu()
listone.add_command(label='New File',command = newf)
listone.add_command(label='Open File')
listone.add_command(label='Save File')
#sub label names
listtwo = Menu()
listtwo.add_command(label='Copy')
listtwo.add_command(label='Past')
listtwo.add_command(label='Undo')
#Adding sub label
menu1.add_cascade(label="File",menu=listone)
menu1.add_cascade(label="Edit",menu=listtwo)
menu1.add_cascade(label="Help")
#calling function
gui.config(menu=menu1)
gui.mainloop()