from multiprocessing import Process
import time

def func(arg1,arg2):
    print('hello,process')
    time.sleep(2)
    print(arg1,arg2)

p = Process(target=func,args=(1,2))
p.start()
print('aha')
p.join()  # 感知子进程的结束，在子进程完成前，他的父进程将一直被阻塞
print('运行完了')
