import json
import socketserver
from core import views

class MySocketServer(socketserver.BaseRequestHandler):
    def handle(self):
        msg = self.my_recv()
        print(msg)
        op_str = msg['operation']
        print(op_str)
        if hasattr(views, op_str):
            getattr(views,op_str)(msg)
    def my_recv(self):
        return json.loads(self.request.recv(1024).decode('utf-8'))
