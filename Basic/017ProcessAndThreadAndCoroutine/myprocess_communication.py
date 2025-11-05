import time
# from queue import Queue
from multiprocessing import Queue,Process,set_start_method
from multiprocessing.queues import Empty


## 初始化队列对象
## 表示最多可以接收三条消息, 为空或者为负值时代表没有上限
# q = Queue(3)
# q.put('爱你到永远')
# q.put('你在做梦')
# print(f'q.full(), {q.full()}')
# q.put('年轻人不讲武德')
# print(f'q.full(), {q.full()}')
#
# print(f'q.qsize(), {q.qsize()}')
# print(f'q.get(), {q.get()}')
# print(f'q.get(), {q.get()}')
# print(f'q.empty(), {q.empty()}')
# print(f'q.get(), {q.get()}')
# print(f'q.empty(), {q.empty()}')
# print(f'q.qsize(), {q.qsize()}')




def wdata(q1, li):
    for i in range(len(li)):
        print(f'{li[i]} 已经被放入')
        q1.put(li[i])
        time.sleep(.2)
    print(f'写入的数据是 {li}')


def rdata(q2):
    while True:
        try:
            data = q2.get(block=False)
            print(f'取出数据 {data}')
        except:
            break
    print(f'读取结束')


if __name__ == '__main__':
    set_start_method("spawn")  # ✅ mac 必加

    li = ['douglas', 'trump', 'hillary', 'clinton']
    q = Queue()

    p1 = Process(target=wdata, args=(q, li))
    p2 = Process(target=rdata, args=(q,))

    p1.start()
    p1.join()  # ✅ 等待写入完成

    p2.start()
    p2.join()

