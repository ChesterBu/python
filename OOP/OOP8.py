# 反射
class BlackMedium:
    feature = 'Ugly'
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
    def rent_house(self):
        print('%s 租房子 ，傻逼才租' %self.name)
    

b1 = BlackMedium('万成置地','天璐园')
# 不has返回false
print(hasattr(b1,'name'))
print(hasattr(b1,'rent_house'))

#不加default ，get不到报错
print(getattr(b1,'name'))
print(getattr(b1,'asdad', 'haha'))
func = getattr(b1,'rent_house')

func()

# b1.sb = True
setattr(b1,'sb',True)

# del b1.sb
delattr(b1,'sb')