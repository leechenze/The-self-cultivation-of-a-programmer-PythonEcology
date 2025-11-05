import time
from multiprocessing import Process

li = []

def wdata():
    for i in range(5):
        li.append(i)
        time.sleep(.2)
    print("写入的数据是: ", li)

def rdata():
    print("读取的数据是: ", li)


if __name__ == '__main__':
    p1 = Process(target=wdata)
    p2 = Process(target=rdata)
    p1.start()
    p2.start()










