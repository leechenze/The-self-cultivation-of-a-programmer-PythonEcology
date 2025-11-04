import os
from multiprocessing import Process

def sing(arg1):
    print(f'{arg1} is sing')
    print(f'sing的进程编号: {os.getpid()}, 父进程编号: {os.getppid()}')

def dance(arg1):
    print(f'{arg1} is dance')
    print(f'dance的进程编号: {os.getpid()}, 父进程编号: {os.getppid()}')

if __name__ == '__main__':
    # 创建子进程
    p1 = Process(target=sing,name='myprocess01', args=('douglas',))
    p2 = Process(target=dance,name='myprocess02', args=('hillary',))
    # 开启
    p1.start()
    p2.start()

    # 这里加join是为了阻塞p1和p2, 让父进程等待p1 和 p2进程执行结束
    # p1.join()
    # p2.join()

    print(f'p1.name: {p1.name}')
    print(f'p2.name: {p2.name}')
    print(f'p1.pid: {p1.pid}')
    print(f'p2.pid: {p2.pid}')

    print(f'p1的存活状态: {p1.is_alive()}')
    print(f'p2的存活状态: {p1.is_alive()}')







































