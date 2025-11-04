from threading import Thread, Lock

a = 0
b = 1000000

lock = Lock()

def add1():
    lock.acquire()
    global a
    for i in range(b):
        a += 1
    print(f'add1执行: {a}')
    lock.release()

def add2():
    lock.acquire()
    global a
    for i in range(b):
        a += 1
    print(f'add2执行: {a}')
    lock.release()


t1 = Thread(target=add1)
t2 = Thread(target=add2)

t1.start()
t2.start()








