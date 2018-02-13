#用with打开的话就不用f.close()了
with open('./login.py','r') as f:
    data = f.read()
    print(data)