
import socket 

sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
 
# Get the old state of the SO_REUSEADDR option 
old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR ) 
print ("Old sock state: ", old_state) 
 
# Enable the SO_REUSEADDR option 
sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 ) 
new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR ) 
print ("New sock state:",new_state) 

local_port = 8080
     
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1) 
srv.bind( ('', local_port) ) 
srv.listen(1) 

print ("Listening on port:",local_port) 
while True: 
    try: 
        connection, addr = srv.accept() 
        print ('Connected by',addr[0])
        rmsg=connection.recv(1024).decode();
        print(rmsg)
    except KeyboardInterrupt: 
        print("keyboard Interrupted.")
        break 
    except socket.error as msg: 
            print (msg) 
 
 
