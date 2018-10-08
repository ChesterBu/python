num = 256
result = ''

# while num > 0:
#     result = str(num % 2) + result
#     num = num//2
# print(result)

dic = {
    'a': 1,
    (1, 2, 3): 2
}
print(dic)

def calc(*numbers):
    print(numbers,type(numbers))
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(calc(1,2,3))
print(calc())


def person(name, age, **kwargs):
    print('name:', name, 'age:', age, 'other:',kwargs)

person(1, 2, a=1)

# l = [1, 2, 3]
# z = l[:]
# z[0] = 0
# print(l) [1, 2, 3]

l = [[1,2], 2, 3]
z = l[:]
z[0][0] = 2
print(l)  #[[2, 2], 2, 3]

li = [x * x for x in range(1, 11) if x % 2 == 0]
print(li)
#print(x)  # name 'x' is not defined

def init(func):
    return func()
    

# @deco1
# @deco2
# @deco3
# def foo():
#     pass
# foo = deco1(deco2(deco3(foo)))

@init #odd = init(odd)
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
    
#g = odd()



print(next(odd))
print(next(odd))


def init2(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper
@init2
def eater(name):
    print(f'{name} 准备吃饭了')
    food_list = []
    while True:
        food = yield food_list
        print(f'{name}吃了{food}')
        food_list.append(food)
g = eater('l')
# s = next(g)
# print(s) 
s = g.send('蒸羊羔')
print(s)
s = g.send('烤羊腿')
print(s)



from sys import path
#print(path)

# import module.a as a
# a.test()

# def ac():
#     import module.a as a

# ac()
# a.test() # name 'a' is not defined

from  module import a 
a.test()

import os

print(os.listdir('../OOP'))
print(os.pathsep)
print(os.linesep)
