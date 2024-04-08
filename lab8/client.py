import socket
import argparse
import sys
 
def udp_client(host, port):

    # Creating socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_address = (host, port)
 
    try:
        while True:
            message = input("Enter message : ")

            client_socket.sendto(message.encode(), server_address)
            data, connection = client_socket.recvfrom(1024)
            print("Received echoed message:",data.decode())
    except KeyboardInterrupt:
        print("\nClosing the client.")
        client_socket.close()
        sys.exit(0)
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UDP Client")
    parser.add_argument("--host", help="Server host address", default="localhost")
    parser.add_argument("--port", help="Server port number", type=int, default=8080)
    args = parser.parse_args()
 
udp_client(args.host, args.port)