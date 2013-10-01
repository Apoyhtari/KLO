from Tkinter import *
import sys
import socket
import string
import threading


#global irc = socket.socket(socket.AF_INET, socket.AF_STREAM)

class Connection:
    """
    This class is intended to be used for connecting to irc via a thread. The calling should be done
    within App. As such, a new thread should also be made for handling the UI
    connectionthread = threading.thread(None, Connection.connect, "ConnThread", params)
    """
    def connect(self):
        """
        Handle connection logic here
        """
        network = 'irc.nebula.fi'
        port = 6667
        self.irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        self.irc.connect ( ( network, port ) )
        self.irc.send ( 'NICK RaivoRaimo\r\n' )
        self.irc.send ( 'USER botty botty botty :Python IRC\r\n' )
        self.irc.send ( 'JOIN #KLOtesti\r\n' )
        print "yaya"
        self.processForever()

    def processForever(self):
        while True: # Be careful with these! It might send you to an infinite loop
            self.ircmsg = self.irc.recv(1024) # receive data from the server
            print(self.ircmsg) # Here we print what's coming from the server
            if self.ircmsg.find ('PING') !=-1:
                self.irc.send('PONG' + self.ircmsg.split() [1] + '\r\n')
        


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
        connection = Connection()
        self.conn = Button(root, text="Connect", width=20, command=connection.connect)
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
        
        
