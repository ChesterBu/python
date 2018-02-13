# python 数字都是int
# python 中一切皆对象

a = 'alex'
b = a.capitalize()
print(a)  # alex
print(b)  # Alex

name = ' aleX'
print(name.strip())
print(name.startswith('al'))
print(name.endswith('X'))
print(name.replace('l', 'p'))
print(name.split('l'))
print(name.upper())
print(name.lower())
print(name[1])
print(name[0:2])
print(name[-2:])
print(name.index('e'))
print(name[:-1])

str_li = 'alexericrain'
print('_'.join(str_li))
li = ['alex', 'eric', 'rain']
print('_'.join(li))


def adder():
    content = input('plesae input:')
    li = content.split('+')
    output = 0
    for item in li:
        item = item.strip()
        output += int(item)
    return output


def lenCounter():
    content = input('please input:')
    srt_num = 0
    int_num = 0
    for item in content:
        if item.isdecimal():
            int_num += 1
        else:
            srt_num += 1
    print(int_num, srt_num)


def template():
    name = input('name:')
    location = input('where:')
    hobby = input('hobby:')
    temp = '{0}{1}{2}'
    print(temp.format(name, location, hobby))


def check_in():
    def check_code():
        import random
        checkcode = ''
        for i in range(4):
            current = random.randrange(0, 4)
            if current != i:
                temp = chr(random.randint(65, 90))
            else:
                temp = random.randint(0, 9)
            checkcode += str(temp)
        return checkcode
    flag = True
    while flag:
        code = check_code()
        print(code)
        check = input('input code:')
        if check == code:
            flag = False
            print('welcome')
        else:
            continue


def filters():
    content = input('input')
    print(content.replace('A','***'))


str
        
