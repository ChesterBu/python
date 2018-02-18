#继承先找自己有没有，没有在找父类的

class Dad:
    money = 100
    def __init__(self,name):
        print('爸爸')
        self.name = name
    
    def hit_son(self):
        print('打')

class Son(Dad):
    money = 1000
    pass


s = Son('alex')
print(s.name)
print(s.money)
s.hit_son()
print(s.__dict__)