



import gevent



def sing():
    print('sing')
    # 模拟被阻塞的情况(比如网络/文件传输/标准输入输出的IO,sleep也是IO,会造成等待的任务都是IO操作)
    gevent.sleep(.5)
    print('i"ve finished song')

def dance():
    print('dancing')
    gevent.sleep(.5)
    print('i"ve finished dancing')



if __name__ == '__main__':
    # 创建协程对象
    g1 = gevent.spawn(sing)
    g2 = gevent.spawn(dance)

    g1.join()
    g2.join()












