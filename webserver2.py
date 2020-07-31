import socket
from handlereq import *

HOST,PORT = 'localhost',8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(0)

print(f"The server is running on port {PORT}...")

connected = True
while connected:
	client,client_addr = s.accept()
	raw_data = client.recv(1024)
	if(len(raw_data)==0):
		print('socket close')
		client.close()
	else:
		data = raw_data.decode('utf-8')
		print(data)
		req_info = getheader(data)
		response = getresponsedata(req_info)
		client.send(response)
		client.close()

