import  socket

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.bind(('127.0.0.1',8080))

while True:
    data = udp.recvfrom(1024)
    print(data)



# udp 没有链接，所以这样写就可以并发了