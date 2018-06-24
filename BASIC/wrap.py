FLAG = False
def login(func):
    def inner(*args,**kwargs):
        global FLAG
        '''登录程序'''
        if FLAG:
            ret = func(*args, **kwargs)  # func是被装饰的函数
            return ret
        else:
            username = input('username : ')
            password = input('password : ')
            if username == 'boss_gold' and password == '22222':
                FLAG = True
                ret = func(*args,**kwargs)      #func是被装饰的函数
                return ret
            else:
                print('登录失败')
    return inner

@login
def shoplist_add():
    print('增加一件物品')

@login
def shoplist_del():
    print('删除一件物品')

shoplist_add()
shoplist_del()