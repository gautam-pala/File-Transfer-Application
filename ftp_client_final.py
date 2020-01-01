import socket
import sys
import os

port=12345
s=socket.socket()
s.connect(("127.0.0.1",port))
msg=raw_input("enter the file name which you want  ")
s.send(msg)
f_size=s.recv(4)
print("file size is : ",f_size)
msg_size=s.recv(4)
print("message size is : ",msg_size)
file_path=raw_input("enter the file path : ")
f=os.open(file_path,os.O_RDWR|os.O_CREAT)
print("file opened")
while True:
	data=s.recv(1024)
	if not data:
		break
	if(data=="not found bye"):
		print(data)
		break
	os.write(f,data)
os.close(f)

