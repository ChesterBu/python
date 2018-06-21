def haha(l=[]):
    l.append(1)
    print(l)


haha() #  [1]
haha() # [1, 1]
haha() # [1, 1, 1]
 # print(l) 报错

def heihie(k,v= {}):
    v[k] = 'v'
    print(v)

heihie(1)  # {1: 'v'}
heihie(2)  # {1: 'v', 2: 'v'}
heihie(3)  # {1: 'v', 2: 'v', 3: 'v'}