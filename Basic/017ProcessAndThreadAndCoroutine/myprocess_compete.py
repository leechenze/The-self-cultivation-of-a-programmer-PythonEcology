from threading import Thread

a = 0
b = 1000000
def add1():
    for i in range(b):
        global a
        a += 1
    print("第一次执行: ", a)

def add2():
    for i in range(b):
        global a
        a += 1
    print("第一次执行: ", a)

# add1()
# add2()

if __name__ == '__main__':
    t1 = Thread(target=add1)
    t2 = Thread(target=add2)

t1.start()
t2.start()

# t1.start() 和 t2.start() 的执行会打印如下
# 第一次执行:  1235795
# 第一次执行:  1184013
# 这不是正常情况, 是因为两个线程共同共同争抢了 全局变量 a, 所以才导致的这种情况
# 这种情况的解决办法就是采取线程同步












