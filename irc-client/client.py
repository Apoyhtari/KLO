from Tkinter import *
import sys

class App:
    def __init__(self, master):
        
        w = Canvas(master, width=500, height=400)
        w.pack()
        w.create_rectangle(10, 350, 500, 10, fill="white")

def callback():
	print "called the callback!"

if __name__ == "__main__":        
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

	e = Entry(root, width=80)
	e.pack()
	e.delete(0, END)
	e.insert(0, "a default value")
	b = Button(root, text="Send", width=10, command=callback)
	b.pack()

	RTitle=root.title("Windows")

	root.geometry("600x600+300+300")

	root.mainloop()

