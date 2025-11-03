import threading

counter = 0

def add():
    global counter
    for _ in range(100000):
        counter += 1

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=add)

t1.start()
t2.start()

# join方法是等待t1任务执行结束, 在t1任务执行结束之前阻塞 print("最终结果：", counter) 打印代码执行
t1.join()
t2.join()

print("最终结果：", counter)





