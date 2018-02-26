import threading
import time

def music():
    print('listen music')
    time.sleep(3)
    print('music end')

def game():
    print('gaming')
    time.sleep(5)
    print('game over')

    

if __name__ == '__main__':
    t1 = threading.Thread(target=music)
    t2 = threading.Thread(target=game)

    t1.start()
    t2.start()
   
    print('end')

    '''
    join():在子线程完成前，他的父线程将一直被阻塞
    setDaemon():必须在start()前调用，守护线程，主线程只要完成了，就结束
    
    
    '''