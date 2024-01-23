
import socket

HOST = "127.0.0.1" 
PORT = 65432 

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
             break;
        conn.sendall(data)


except socket.error as error:
    print(error)


    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)