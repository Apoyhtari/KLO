from Tkinter import *
import sys
import socket
import string
import threading
import connection

class App:
    
    def __init__(self, master):		
        self.w = Canvas(master, width=500, height=400)
        self.w.pack()
        self.w.create_rectangle(10, 350, 500, 10, fill="white")
        self.canvas_id = self.w.create_text(15, 10, anchor="nw")
        self.e = Entry(root, width=80)
        self.e.pack()
        self.e.delete(0, END)
        self.e.insert(0, "a default value")
        self.s = self.e.get()
        self.b = Button(root, text="Send", width=10, command=self.callback)
        self.b.pack()
        self.w.itemconfig(self.canvas_id, text=self.s)
        self.w.insert(self.canvas_id, 12, "")
        self.w.update()
        self.conn = Button(root, text="Connect", width=20, command=self.connect)
        self.conn.pack()        
        	
    def callback(self):
        self.s += "\n" +self.e.get()
        self.w.itemconfig(self.canvas_id, text=self.s)
        self.w.update()
        Self.irc.send('PRIVMSG #lollipopguild :' +self.e.get()+' \r')
	
if __name__ == "__main__":    
        root = Tk()
        app = App(root)
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
        
        
