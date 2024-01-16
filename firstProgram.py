import socket

# to get the machine name
machine_name=socket.gethostname()
print(f"The machine's name is :{machine_name}")

# to get the ip address
ip_addr=socket.gethostbyname(machine_name)
print("The IPV4 address is : "+ ip_addr) 

a=socket.getaddrinfo(ip_addr)
print(a)