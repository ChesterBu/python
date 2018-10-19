import time
from multiprocessing import Process

def func():
    while True:
        time.sleep(0.2)
        print('still alive')

if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True  #设置子进程为守护进程
    p.start()
    i = 0
    while i < 5:
        print('socket server')
        time.sleep(1)
        i += 1
        
