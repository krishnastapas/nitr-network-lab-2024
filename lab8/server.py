import socket
import argparse
import sys
 
def udp_server(host, port):
    # Create  UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
    server_address = (host, port)
    server_socket.bind(server_address)
 
    
 
    while True:
        print("Waiting for a message from the client...")
        data, client_address = server_socket.recvfrom(1024)  
 
        print("Received message:", data.decode())
 
        server_socket.sendto(data, client_address)
 
    
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UDP Server")
    parser.add_argument("--host", help="Server host address", default="localhost")
    parser.add_argument("--port", help="Server port number", type=int, default=8080)
    args = parser.parse_args()
 
    try:
        udp_server(args.host, args.port)
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)