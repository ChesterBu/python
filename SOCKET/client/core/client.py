from core.auth_client import Auth

def main():
    auth = None
    start_menu = [('登录','login'), ('注册','register'), ('退出','exit')]
    for index, item in enumerate(start_menu, 1):
        print(index, item[0])
    while True:
        try:
            num = int(input('>>'))
            func_str = start_menu[num - 1][1]
            print(func_str)
        except:
            print('输入信息有误')
        if hasattr(Auth, func_str):
            auth = Auth(('127.0.0.1', 8080))
            res = getattr(auth, func_str)()
            if res: break
        elif auth:
            auth.sk.close()
            exit()
        else:
            exit()

