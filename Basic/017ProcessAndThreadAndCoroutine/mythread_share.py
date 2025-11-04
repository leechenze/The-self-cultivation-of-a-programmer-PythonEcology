
import time
from threading import Thread

### 线程之间共享资源
li = []
# 写数据
def wdata():
    for i in range(5):
        li.append(i)
        time.sleep(.2)
    print("写入的数据是: ", li)
# 读数据
def rdata():
    print("读取的数据是: ", li)


if __name__ == '__main__':
    # 创建子线程
    t1 = Thread(target=wdata)
    t2 = Thread(target=rdata)
    # 开启子线程
    t1.start()
    # 阻塞线程, join方法是等待t1任务执行结束
    # t1.join()
    # 或者如果不阻塞的话也可以直接指定让 t2 读取线程等待指定的秒数, 比如如果是 0.8 秒 就只会读到3就结束.
    time.sleep(.8)
    t2.start()
