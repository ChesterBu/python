from core.socket_client import SocketClient 
class Auth:

    __instance = None

    def __new__(cls, *args, **kwargs):
        #单例模式
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,addr):
        self.sc = SocketClient(addr)
        self.sk = self.sc.sk

    def login(self):
        username = input('username:')
        password = input('password:')
        if username.strip() and password.strip():
            self.sc.send_msg({'username': username, 'password': password,'operation':'login'})
        return self.sk.recv(1024)

    def regester(self):
        username = input('username:')
        password1 = input('password:')
        password2 = input('password ensure:')
        if username.strip() and password1.strip() and password1 == password2:
            self.sc.send_msg({'username': username, 'password': password1, 'operation': 'regester'})
        return self.sk.recv(1024)
