#OOD 面向对象设计


def Cat(name,gender):
    def init(name,gender):
        cat = {
            'name':name,
            'gender':gender,
            'jiao':jiao
        }
        return cat
    def jiao(cat):
        print('%s：喵喵喵' %cat['name'])

    return init(name,gender)


cat = Cat('tom','male')
cat['jiao'](cat)





# OOP 面向对象编程

class Dog:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    
    def bark(self):
        print('%s is barking' %self.name)


dog = Dog('tom','male')

dog.bark()



# 类

class Chinese:
    # 这是一个中国人类
    dang = 'gcd' #静态属性

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
print(p.dang)  #实例可以调用类属性
# print(p.sui_di_tu_tan())  #报错
p.cha_dui()  #实例可调用

#del Chinese.dang   #删除类属性

p.dang = 'GCD'   #相当与给p加了个属性，而不是修改类上的
print(Chinese.dang) # gcd