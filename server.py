import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="127.0.0.1"
port=4000
s.bind((ip,port))
print("server is listening {}".format(s.getsockname()))

while True:
    data,addr=s.recvfrom(1024)
    print('connection from', addr)
    data=data.decode("ascii")
    print("Receved data: ",data)
    send_data="Thanks for your connection."
    send_data=send_data.encode('ascii')
    s.sendto(send_data,addr)
