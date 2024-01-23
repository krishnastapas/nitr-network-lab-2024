import socket
import argparse 
import sys

parser=argparse.ArgumentParser(description="Scoket error ex.")
parser.add_argument('--host',action="store",dest="host",required=False)
args=parser.parse_args()
host=args.host
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def socket_connection(host,port):
    try:
        # creating a socket
        s.connect((host,port))
        print(f"Connected suceessfully to port {port}.................")
    except socket.error as msg:
        print(msg)

def send_data(filename):
    try:
        msg="GET %s HTTP/1.0\r\n\r\n" % filename
        s.sendall(msg.encode('utf-8'))
        print("Message sended sucessfully.")
        # s.sendall(filename)
    except socket.error as msg:
        print(msg)
        sys.e

def receive_data(size):
    try:
       print("Message receive starts...............")
       buf=s.recv(size)
       print(buf)
    except socket.error as msg:
        print("the error occured",msg)

# setting the timeout 
socket.setdefaulttimeout(200)

port=80
socket_connection(host,port);
current_time=socket.getdefaulttimeout()

print(current_time)

filename="send a a messsage"
send_data(filename)

receive_data(2048)





