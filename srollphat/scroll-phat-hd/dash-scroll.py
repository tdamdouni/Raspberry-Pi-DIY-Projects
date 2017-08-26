from pydhcplib.dhcp_network import *
import signal
import os

def do_something():
	os.system('/home/pi/Desktop/hello.py')
	print("button has been pressed")

netopt = {'client_listen_port':"68", 'server_listen_port':"67", 'listen_address':"0.0.0.0"}

class Server(DhcpServer):
	def __init__(self, options, dashbuttons):
		DhcpServer.__init__(self, options["listen_address"],
								options["client_listen_port"],
								options["server_listen_port"])
		self.dashbuttons = dashbuttons

	def HandleDhcpRequest(self, packet):
		mac = self.hwaddr_to_str(packet.GetHardwareAddress())
		self.dashbuttons.press(mac)


	def hwaddr_to_str(self, hwaddr):
		result = []
		hexsym = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
		for iterator in range(6) :
			result += [str(hexsym[hwaddr[iterator]/16]+hexsym[hwaddr[iterator]%16])]
		return ':'.join(result)

class DashButtons():
	def __init__(self):
		self.buttons = {}

	def register(self, mac, function):
		self.buttons[mac] = function

	def press(self, mac):
		if mac in self.buttons:
			self.buttons[mac]()
			return True
		return False

		
dashbuttons = DashButtons()
dashbuttons.register("ac:63:be:ef:cc:fd", do_something)
server = Server(netopt, dashbuttons)

while True:
	  server.GetNextDhcpPacket()
