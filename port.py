import socket
ip=input("Enter your IP:")
port=int(input("Enter the port:"))

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex((ip, port)):
    print("Port", port, "is off")
else:
    print("Port", port, "is on")