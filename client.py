import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
send_data="Hello"
send_data=send_data.encode('ascii')
s.sendto(send_data,('127.0.0.1',4000))
recv_data= s.recv(1024)
recv_data=recv_data.decode('ascii')
print(recv_data)
s.close()
