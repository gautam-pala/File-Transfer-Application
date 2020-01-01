import socket
import sys
import os
import _thread

port=12345
s=socket.socket()
s.bind(('',port))
s.listen(5)
def new_thread(c):
	print("connection established from " ,addr[0])
	data=c.recv(1024)
	print(data)
	if (os.path.isfile(data)):
		f_info=os.stat(data)
		size=str(f_info.st_size)
		c.send(size)
		message_size="1024"
		c.send(message_size)
		f=os.open(data,os.O_RDWR|os.O_CREAT)
		l=os.read(f,1024)
		while (l):
			if not l:
				break
			c.send(l)
			print("1024 bytes data of file are sent")
			l=os.read(f,1024)
		os.close(f)
	else:
		c.send("not found bye")
	c.close()
	
while True:
	c,addr=s.accept()
	_thread.start_new_thread(new_thread,(c,))
	
