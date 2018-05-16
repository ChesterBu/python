username = 'alex'
passwd = '123'
times = 3
while times:
    u = input('please input your username:')
    p = input('please input your passwd:')
    if u == username and p == passwd:
        break
    else:
        print('wrong')
        times -= 1
if times == 0:
    print('byebye')
else:
    print('welcome login')
