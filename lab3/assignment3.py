import socket
import argparse 
import sys


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def socket_connection(host,port):
    try:
        # creating a socket
        s.connect((host,port))
        print(f"Connected suceessfully to port {port}.................")
    except socket.error as msg:
        print(msg)
        sys.exit()

def send_data(filename):
    try:
        msg="GET %s HTTP/1.0\r\n\r\n" % filename
        s.sendall(msg.encode('utf-8'))
        print("Message sended sucessfully.")
        # s.sendall(filename)
    except socket.error as msg:
        print(msg)
        sys.exit()
        

def receive_data(size):
    try:
       print("Message receive starts...............")
       buf=s.recv(size)
       print(buf)
    except socket.error as msg:
        print("the error occured",msg)
        sys.exit()



parser=argparse.ArgumentParser(description="Scoket error ex.")
parser.add_argument('--host',action="store",dest="host",required=False)
# parser.add_argument('--port',action="store",dest="port",required=False)
parser.add_argument('--msg',action="store",dest="msg",required=False)
args=parser.parse_args()
host=args.host
# port=args.port
msg=args.msg
port=80
# print(host)
# print(port)
# print(msg)
# setting the timeout 
socket.setdefaulttimeout(200)

socket_connection(host,port);
current_time=socket.getdefaulttimeout()

print(current_time)

# msg="send a a messsage"
send_data(msg)

receive_data(2048)





