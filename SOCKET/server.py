import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
conn,addr = sk.accept()
ret = conn.recv(1024)
print(ret)
conn.send(b'hi')
conn.close()
sk.close()

