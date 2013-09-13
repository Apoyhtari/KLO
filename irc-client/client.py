from Tkinter import *
import sys

class App:
    def __init__(self, master):
        w = Label(root, text="HELLO!!")
        w.pack()

    def callback():
        print "called the callback!"


   
root = Tk()
app = App(root) 
# create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="new")
filemenu.add_command(label="open...")
filemenu.add_separator()
filemenu.add_command(label="exit")

e = Entry(root)
e.pack()
e.delete(0, END)
e.insert(0, "default")

e.focus_set()

def callback():
    print e.get()

b = Button(root, text="get", width=10, command=callback)
b.pack()
RTitle=root.title("Windows")

root.geometry("600x600+300+300")



root.mainloop()

