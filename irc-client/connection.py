import sys
import socket
import string

class Connection:
	def __init__(self):
		self.irc = socket.socket(socket.AF_INET, socket.AF_STREAM)
		self.network = ""
		self.port = 6667
		self.nick = ""

	def connect(self, irc, network, port):
		"""
		Handle connection logic here
		"""
		self.irc.send((self.network, self.port))
		#self.irc.send("NICK RaivoRaimo\r\n")
		#self.irc.send("USER botty botty botty; Python IRC\r\n")
		#self.irc.send("JOIN #lollipopguild\r\n")

