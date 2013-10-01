import sys
import socket
import string

class Connection:
	def __init__(self):
		self.irc = socket.socket(socket.AF_INET, socket.AF_STREAM)
		self.network = "irc.nebula.fi"	#default network
		self.port = 6667
		self.nick = ""

	def connect(self, irc, network, port):
		"""
		Handle connection logic here
		"""
		self.irc.send((self.network, self.port))
		self.irc.send("NICK RaivoRaimo\r\n")
		self.irc.send("USER botty botty botty :Python IRC\r\n")
		self.irc.send("JOIN #lollipopguild\r\n")

	def processForever(self):
		while True:
			self.ircmsg = self.irc.recv(1024)	#receive data
			print(self.ircmsg)
			if self.ircmsg.find("PING") != -1:
				self.irc.send("PONG" + self.ircmsg()[1] + "\r\n")


