import socket
import argparse 
import sys


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def socket_connection(host,port):
    try:
        s.connect((host,port))
        print(f"Connected suceessfully to port {port}.................")
    except socket.error as msg:
        print(msg)
        print("Cannot connect...........")
      


host="www.google.com"
port=80
SEND_BUF_SIZE=2308
RECV_BUF_SIZE=4500

print("-----Buffer size before----------")
send_bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF) 
receive_bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF) 
print ("Send Buffer size :",send_bufsize) 
print ("Receive Buffer size :",receive_bufsize) 

s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF,SEND_BUF_SIZE) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF,RECV_BUF_SIZE) 

print("-----Buffer size after----------")
send_bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF) 
receive_bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF) 
print ("Send Buffer size :",send_bufsize) 
print ("Receive Buffer size :",receive_bufsize) 

s.setblocking(0)
socket_connection(host,port)

s.setblocking(1)
socket_connection(host,port)

