

from collections.abc import Iterable


string = '123'
print(f'isinstance(string, str), {isinstance(string, str)}')
print(f'isinstance(string, Iterable), {isinstance(string, Iterable)}')
print(f'isinstance(123, int), {isinstance(123, int)}')
# 意思如果123是 int 或 str 类型都会返回True
print(f'isinstance(123, (int,str)), {isinstance(123, (int,str))}')
print('\n')



### 迭代器
# 方式一
li = [1,2,3,4,5]
l1 = iter(li)
print(f'l1, {l1}')
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))


# 方式二
l2 = li.__iter__()
print(f'l2, {l2}')
print(l2.__next__())
print(l2.__next__())
print(l2.__next__())
print(l2.__next__())
print(l2.__next__())
print('\n')


### 自定义迭代类
class MyIterator(object):
    def __init__(self):
        self.num = 0
    def __iter__(self):
        # 返回当前迭代器的实例对象
        return self
    def __next__(self):
        if self.num == 10:
            raise StopIteration("终止迭代器")
        self.num += 1
        return self.num

mi = MyIterator()
print(f'mi, {mi}')
# print(f'next(mi), {next(mi)}')

for i in mi:
    print(f'i, {i}')
print('\n')







### 生成器
### 生成器表达式, 类似于列表推导式
gen = (i*5 for i in range(5))
print(f'gen, {gen}')
print(f'dir(gen), {dir(gen)}')

print(f'next(gen),{next(gen)}')



### 生成器函数
def gen1():
    yield 'a'
    yield 'b'
    yield 'c'
gen01 = gen1()
print(gen01)
print(next(gen01))
print(next(gen01))
print(next(gen01))


def gen2(n):
    li = []
    for i in range(n):
        li.append(i)
    print(f'li, {li}')
gen2(5)


def gen3(n):
    li = []
    for i in range(n):
        yield i

gen03 = gen3(5)
print(next(gen03))
print(next(gen03))
print(next(gen03))
print(next(gen03))
print(gen03.__next__())




















