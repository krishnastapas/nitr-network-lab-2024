import socket
import datetime
local_port=8080
HOST = '127.0.0.1'

sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 

sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1) 
sock.bind( (HOST, local_port) ) 
sock.listen(5) 

print ("Listening on port:",local_port) 
client_connections = {}
last_time=0
while True: 
    try: 
        connection, addr = sock.accept() 
        print ('Got connection from', addr[0], addr[1])
        if addr[0] in client_connections:
            client_connections[addr[0]] += 1
        else:
            client_connections[addr[0]] = 1
        last_time = datetime.datetime.now()
        connection.recv(1024)
        connection.send(b'HTTP/1.0 200 OK\n')
        connection.send(b'Content-Type: text/html\n')
    
        response=f"""
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h5>The host name and ip are {socket.gethostname()} and {addr[0]}</h5>
<p> count: {client_connections[addr[0]]  } </p>


</body>
</html>"""
        
        connection.sendall(response.encode('utf-8'))
        connection.close()
        
    except KeyboardInterrupt: 
        print("keyboard Interrupted.")
        break 
    except socket.error as msg: 
            print (msg)