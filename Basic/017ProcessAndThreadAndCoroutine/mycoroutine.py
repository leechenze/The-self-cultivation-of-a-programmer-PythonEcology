


def task1():
    yield 'a'
    yield '哈哈哈'
def task2():
    yield 'b'
    yield '嘿嘿嘿'
if __name__ == '__main__':
    t1 = task1()
    print(t1)
    t2 = task2()
    print(next(t1))
    print(next(t1))
    print(next(t2))
    print(next(t2))































