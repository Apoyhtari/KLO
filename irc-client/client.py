from Tkinter import *
import sys

class App:
    def __init__(self, master):
        
        w = Canvas(master, width=500, height=400)
        w.pack()
        w.create_rectangle(10, 350, 500, 10, fill="white")
        canvas_id = w.create_text(15, 10, anchor="nw")
        e = Entry(root, width=80)
        e.pack()
        e.delete(0, END)
        e.insert(0, "a default value")
        s = e.get()
        b = Button(root, text="Send", width=10, command=callback)
        b.pack()
        w.itemconfig(canvas_id, text=s)
        w.insert(canvas_id, 12, "")
        w.update()

        
def callback():
	print e.get()
	print s
	

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
	
	
	
	

	
	       
	
	
	RTitle=root.title("Windows")

	root.geometry("600x600+300+300")

	root.mainloop()

