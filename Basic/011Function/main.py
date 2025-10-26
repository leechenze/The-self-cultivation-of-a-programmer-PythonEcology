import builtins
import functools

# 可变参数
def func(*args):
    print(args,type(args))
    print(args[1])
func(1,2,'3')


# 关键字参数
print('\n')
def func1(**kwargs):
    print(kwargs, type(kwargs))
func1()
func1(name='anglee',age = 20)


# 函数嵌套
print('\n')
def study():
    print('learning in evening')
    def course():
        print('python base')
    course()
study()


# 作用域
# 全局变量
print('\n')
a = 100
def func2():
    print('func2中a的值是: ', a)
def func3():
    # a = 120
    global a
    a = 120
    print('func3中a的值是: ', a)
print("调用前a的值: ", a)
func2()
func3()
print("调用后a的值: ", a)


# nonlocal
print('\n')
b = 10
def outer():
    b = 5
    def inner():
        nonlocal b
        b = 20
        print("inner函数中b的值是: ", b)
    inner()
    print("outer函数中b的值是: ", b)
outer()


# 匿名函数
print('\n')
add = lambda a,b:a+b
print(add(2,3))

res = lambda : '无参匿名函数'
print(res())

func4 = lambda name,age = 18:(name,age)

func5 = lambda **kwargs:kwargs['name'] + '-' + str(kwargs['age'])
print(func5(name='anglee',age=20))


# lambda结合if和else
print('\n')
a1 = 5; b1 = 8
print('b大') if a1<b1 else print("a大")
res = lambda a, b : 'b大' if a1<b1 else "a大"
print('res值为: ', res(a1,b1))


### 内置函数
print('\n')
print(dir(builtins))

print(max(4,1,8,-2))
print(min(4,1,8,-2))
# 表示用绝对值进行取最小值
print(min(4,1,8,-2,key=abs))

# zip
list0 = [1,2,3]
list1 = ['a','b','c']
tuple0 = ('a','b','c')
print(zip(list0,list1))
print(zip(list0,list1))
print("list(zip(list0,list1))的值为: ",list(zip(list0,list1)))
# 如果两个序列长度不一样时, 就以长度最短的为准返回
for i in zip(list0,list1):
    print(i)


# map
print('\n')
list2 = [1,2,3,4,5]
def func6(x):
    return x * 5
func7 = lambda x : x + 5
res = map(func7, list2)
res1 = map(lambda x:x+5, list2)
print(list(res))
print(list(res1))



# reduce
print('\n')
list3 = [1,2,3]
add = lambda a,b:a+b
print(functools.reduce(add, list3))



### 拆包
print('\n')
tup0 = (1,2,3,4)

a,b,c,d = tup0
print(a, b, c, d)

a,*b, = tup0
print(a,b)

def func8(*args):
    print(args)

print('tup0',tup0)
print('*tup0', *tup0)
print(func8(*tup0))


