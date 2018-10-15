import socket
import json
class SocketClient:

    def __init__(self,addr):
        self.sk = socket.socket()
        self.sk.connect(addr)

    def send_msg(self, msg):
        self.sk.send(json.dumps(msg).encode('utf-8'))
