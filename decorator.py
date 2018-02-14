import time
# def timmer(func):   #不可传参的装饰器
#     def wrapper(*arg,**kwargs):
#         start_time = time.time()
#         res = func(*arg,**kwargs)
#         end_time = time.time()
#         print('running time is %s'%(end_time-start_time))
#         return res   #防止func有返回值
#     return wrapper

def timmerX(a):       #可以传参数的装饰器
    def timmer(func):
        def wrapper(*arg,**kwargs):
            if(a==1):
                start_time = time.time()
                res = func(*arg,**kwargs)
                end_time = time.time()
                print('running time is %s'%(end_time-start_time))
                return res   #防止func有返回值
            else:
                print('a is not 1')
        return wrapper
    return timmer


@timmerX(1)
def a():
    time.sleep(3)
    print('a func done')

a()