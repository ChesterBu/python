import socket
# sk = socket.socket()
# sk.connect(('127.0.0.1', 8080))
# sk.send(b'hello')
# ret = sk.recv(1024)
# print(ret)
# sk.close()

#print(type('b'.encode('utf-8')))  # <class 'bytes'>

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8080))
while True:
    cmd = input('>>')
    if cmd.strip() == 'q':
        sk.send(b'q')
        break

    sk.send(cmd.encode('utf-8'))
    res = sk.recv(1024)
    print(res.decode('utf-8'))
