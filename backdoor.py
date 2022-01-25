#!usr/bin/python
# -*- coding: utf-8 -*-

import socket 

class backdoor(object):
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = "localhost"
		self.port = 6890
		self.key = "12345"

	def main(self):
		while True:
			try:
				self.sock.connect((self.host, self.port))
				break
			except socket.error as msg:
				pass
		self.sock.send(self.key)
		comando = self.sock.recv(4096)
		print comando

if __name__ == "__main__":
	app = backdoor()
	app.main()

