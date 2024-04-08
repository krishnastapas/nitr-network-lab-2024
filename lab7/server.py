import socket
local_port=8080


sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 

sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1) 
sock.bind( ('', local_port) ) 
sock.listen(1) 

print ("Listening on port:",local_port) 

while True: 
    try: 
        connection, addr = sock.accept() 
        print ('Connected by',addr)
        rmsg=connection.recv(1024).decode();
        print(rmsg)
        rmsg="Message I recieved :"+rmsg
        connection.send(rmsg.encode());
        
    except KeyboardInterrupt: 
        print("keyboard Interrupted.")
        break 
    except socket.error as msg: 
            print (msg)