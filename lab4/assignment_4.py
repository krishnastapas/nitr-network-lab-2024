# Printing the current time from the internet time server with the help of NTP?
# Also write an SNTP client that prints the current time from the internet time
# server received with the SNTP protocol?
import ntplib
from time import ctime
import time
import socket
import struct
import sys
 
NTP_SERVER="0.in.pool.ntp.org"
TIME1970=2208988800
 
s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
 
def socket_connection(host,port):
    try:
        # creating a socket
        s.connect((host,port))
        print(f"Connected suceessfully to port {port}.................")
    except socket.error as msg:
        print(msg)
        sys.exit()
 
 
def time_from_ntp():
    try:
        c = ntplib.NTPClient()
        response = c.request(NTP_SERVER)
        print("Time received from NTP server:",ctime(response.tx_time))
    except ntplib.NTPException as msg:
        print(msg)
 
dob =908949600
def time_from_server(server,port):
    
    data='\x1b' + 47*'\0'
 
    # socket_connection(server,port)
    s.sendto(data.encode('utf-8'), (server, port))
    data, address = s.recvfrom( 1024 )

    epoch = struct.unpack('!12I', data)[10] - TIME1970
    print("The SNTP client current time is ",ctime(epoch))


    print("The Date of birth is :",ctime(dob))

    age_seconds = epoch - dob
    age_years = age_seconds / (365.25 * 24 * 60 * 60)  # assuming a year has 365.25 days on average
    print("The age is approximately (in years) :",format(age_years))
 
time_from_ntp()
    
server="time1.google.com"
port=123
time_from_server(server,port)