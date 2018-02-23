import  socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))


while True:

    msg = input('>>:')
    phone.send(msg.encode('utf8'))
    print('已发送数据')
    data = phone.recv(1024)

    print('server send ', data.decode('utf8'))


