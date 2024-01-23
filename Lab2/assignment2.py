import socket
import binascii
def get_remote_ip(remote_host):
    try:
        remote_ip=socket.gethostbyname(remote_host)
        return remote_ip
    except:
        print("Error")

# 
def convert_IP_address_format(ip_addr):
    try:
        # print(ip_addr)
        ipPacket=socket.inet_aton(ip_addr)
        new_ip=binascii.hexlify(ipPacket)
        return new_ip
    except :
        print("Error")    

def convert_IP_address_hexa_to_normal(ip_addr):
    try:
        # print(ip_addr)
        ipPacket=binascii.unhexlify(ip_addr)
        new_ip=socket.inet_ntoa(ipPacket)
        return new_ip
    except :
        print("Error")  
        
# service name of a port
def get_service_name(port,protocol):
    try:
        service_name=socket.getservbyport(port,protocol)
        return service_name
    except: 
        print("Error")


# get the remote host IP
remote_host="www.google.com"
remote_ip=get_remote_ip(remote_host)
print(f"The IP address of {remote_host} is : {remote_ip}")

# conversion
con_ip=convert_IP_address_format(remote_ip)
print(f"The actual ip address in hexa decimal {con_ip}")

ip=convert_IP_address_hexa_to_normal(con_ip);
print(f"The revert IP from Hexa value is :{ip}")

# get the service name
# for port in range(1000):
#     service_name=get_service_name(port,"tcp")
#     print(f"The service name of port no {port} is {service_name}")


service_name=get_service_name(20,'tcp')
print(f"The service name of port no {20} is {service_name}")