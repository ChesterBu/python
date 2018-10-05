# OOD 面向对象设计


def Cat(name, gender):
    def init(name, gender):
        cat = {
            'name': name,
            'gender': gender,
            'jiao': jiao
        }
        return cat

    def jiao(cat):
        print('%s：喵喵喵' % cat['name'])

    return init(name, gender)


cat = Cat('tom', 'male')
cat['jiao'](cat)


# OOP 面向对象编程

class Dog:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        print(dir(self)) 
        '''
        '__class__', 
        '__delattr__',
        '__dict__',
        '__dir__', 
        '__doc__', 
        '__eq__', 
        '__format__', 
        '__ge__', 
        '__getattribute__', 
        '__gt__', 
        '__hash__', 
        '__init__', 
        '__init_subclass__', 
        '__le__', 
        '__lt__', 
        '__module__',
        '__ne__', 
        '__new__', 
        '__reduce__', 
        '__reduce_ex__', 
        '__repr__', 
        '__setattr__', 
        '__sizeof__', 
        '__str__', 
        '__subclasshook__', 
        '__weakref__', 
        以上都为内置私有方法
        'bark',
        'gender',
        'name'
        '''
    def bark(self):
        print('%s is barking' % self.name)


dog = Dog('tom', 'male')

dog.bark()


# 类

class Chinese:
    # 这是一个中国人类
    dang = 'gcd'  # 静态属性

    # def sui_di_tu_tan():
    #     print('朝着墙上就是一口痰')

    def cha_dui(self):
        print('插队')


print(Chinese.dang)
# Chinese.sui_di_tu_tan()
print(dir(Chinese))
# print(Chinese.__dict__)
print(Chinese.__dict__['dang'])

p = Chinese()
print(dir(p))
print(p.dang)  # 实例可以调用类属性
# print(p.sui_di_tu_tan())  #报错
p.cha_dui()  # 实例可调用

# del Chinese.dang   #删除类属性

p.dang = 'GCD'  # 相当与给p加了个属性，而不是修改类上的
print(Chinese.dang)  # gcd

a = {}
print(dir(a))
'''
'__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
'''


# class Ea:
#     def __init__(self,name):
#         self.name = name

# a1 = Ea('a')

# class Eaa(a1):  #报错
#     def __init__(self):
#         super().__init__()

