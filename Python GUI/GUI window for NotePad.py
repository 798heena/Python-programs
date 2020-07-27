#Python program to create a GUI window for NotePad

from tkinter import*
gui = Tk()
gui.title("Untitled - Notepad")
gui.geometry("500x500+400+200")
menu1 = Menu()
listone = Menu()
listone.add_command(label='New                               Ctrl+N')
listone.add_command(label='New Window     Ctrl+Shift+N')
listone.add_command(label='Open                              Ctrl+O')
listone.add_command(label='Save                                Ctrl+S')
listone.add_command(label='Save As..              Ctrl+Shift+S')
listone.add_command(label='--------------------------------')
listone.add_command(label='Page Setup...')
listone.add_command(label='Print...                             Ctrl+P')
listone.add_command(label='--------------------------------')
listone.add_command(label='Exit')

listtwo = Menu()
listtwo.add_command(label='Undo')
listtwo.add_command(label='---------------------')
listtwo.add_command(label='Cut')
listtwo.add_command(label='Copy')
listtwo.add_command(label='Paste')
listtwo.add_command(label='Delete')

list3 = Menu()
list3.add_command(label='Word Wrap')
list3.add_command(label='Font...')

list4 = Menu()
list4.add_command(label='Zoom')
list4.add_command(label='Status Bar')

list5 = Menu()
list5.add_command(label='View Help')
list5.add_command(label='Send Feedback')
list5.add_command(label='---------------------------')
list5.add_command(label='About Notepad')

menu1.add_cascade(label="File",menu=listone)
menu1.add_cascade(label="Edit",menu=listtwo)
menu1.add_cascade(label="File",menu=list3)
menu1.add_cascade(label="Edit",menu=list4)
menu1.add_cascade(label="Help",menu=list5)

gui.config(menu=menu1)

gui.mainloop()
