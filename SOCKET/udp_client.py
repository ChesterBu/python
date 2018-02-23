from socket import *

udp = socket(AF_INET,SOCK_DGRAM)

while True:
    msg = input('>>')
    udp.sendto(msg.encode('utf8'),('127.0.0.1',8080))


