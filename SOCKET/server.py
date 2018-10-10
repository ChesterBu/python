import socket
import subprocess
# sk = socket.socket()
# sk.bind(('127.0.0.1', 8080))
# sk.listen()
# conn,addr = sk.accept()
# ret = conn.recv(1024)
# print(ret)
# conn.send(b'hi')
# conn.close()
# sk.close()

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #传输方式：网络，方式：tcp
sk.bind(('127.0.0.1', 8080))
sk.listen()
conn, addr = sk.accept()
print('客户端', addr)
while True:
    cmd = conn.recv(1024)
    if len(cmd) == 0 or cmd.decode('utf-8') == 'q':
        break
    print(cmd)
    res = subprocess.Popen(cmd.decode('utf-8'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stderr = res.stderr.read()
    stdout = res.stdout.read()
    conn.send(stderr)
    conn.send(stdout)
    
conn.close()
sk.close()
