import socket
import argparse

local_port=8080

argparser = argparse.ArgumentParser(description='server client using socket python')
argparser.add_argument('-m', action="store", dest='a')

args = argparser.parse_args()
# print(args.a)
msg=args.a
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
sock.connect(('127.0.0.1',local_port))
sock.send(msg.encode())
print(sock.recv(1024).decode())
   


