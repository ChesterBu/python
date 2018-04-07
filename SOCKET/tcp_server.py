import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('127.0.0.1', 8080))

phone.listen(5)
while True:
    print('sever running')
    conn, address = phone.accept()
    print('双向链接是', conn)
    print('客户端地址是', address)

    while True:
        msg = conn.recv(1024)
        if not msg: break
        print('client send ', msg.decode('utf8'))
        conn.send(msg.upper())
    conn.close()  # 断开连接

phone.close()  # 关闭程序
