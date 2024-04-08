# Printing the current time from the internet time server with the help of NTP?
# Also write an SNTP client that prints the current time from the internet time 
# server received with the SNTP protocol? 
import ntplib
from time import ctime

import socket
import struct
import sys
import time

NTP_SERVER="0.uk.pool.ntp.org"
TIME1970=2208988800

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

def socket_connection(host,port):
    try:
        # creating a socket
        s.connect((host,port))
        # print(f"Connected suceessfully to port {port}.................")
    except socket.error as msg:
        print(msg)
        sys.exit()


def time_from_ntp():
    try:
        c = ntplib.NTPClient()
        response = c.request(NTP_SERVER)
        ctime(response.tx_time)
    except ntplib.NTPException as msg:
        print(msg)

def time_from_server(server,port):
    
    data='\x1b' + 47*'\0'

    # socket_connection(server,port)
    s.sendto(data.encode('utf-8'), (server, port))
    data, address = s.recvfrom( 1024 )
    print(data)
    print(address)

# time_from_ntp()
    
server="google.com"
port=123
time_from_server(server,port)