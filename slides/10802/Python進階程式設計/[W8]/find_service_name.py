import socket

def find_service_name():
	protocolname = 'tcp'
	for port in range(80,999):
		try:
			print("Port: %s => service name: %s" %(port, socket.getservbyport(port, 'tcp')))
		except socket.error as err_msg:
			print("Port: %s => service name: %s" %(port, socket.getservbyport(port, 'udp')))
		
	
	#print("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'tcp')))

if __name__ == '__main__':
	find_service_name()