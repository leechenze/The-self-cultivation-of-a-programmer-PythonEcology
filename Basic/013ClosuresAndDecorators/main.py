### 递归函数
# 前n个自然数的和
def add(n):
    if n == 1:
        return 1
    return n + add(n - 1)


print(add(100))


# 非波那契数列
# 1,1,2,3,5,8,13....
def fibonacci(n):
    if n <= 1:
        return n;
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(6))


### 闭包
def outer(m):
    n = 10

    def inner(o):
        return m + n + o

    return inner


inner = outer(20)
print(inner(30))


### 装饰器
# 需求, 注册完成后自动登录,自动登录后自动打卡
# print('\n')
# def checkIn():
#     print("自动打卡")
#
# def login(checkInFn):
#     print("自动登录")
#     checkInFn()
#
# def register(loginWrapperFn):
#     print("开始注册")
#     loginWrapperFn()
#
# register(lambda : login(checkIn))


# 闭包版装饰器
# auto_chain 就是之前 register 函数
# print('\n')
# def auto_chain(loginFn):
#     def wrapper(checkInFn):
#         print("开始注册")
#         loginFn(checkInFn)
#     return wrapper
# def checkIn():
#     print("自动打卡")
# def login(checkInFn):
#     print("自动登录")
#     checkInFn()
#
# auto_chain(login)(checkIn)


# 语法糖装饰器
# print('\n')
# def auto_chain(fn):
#         def wrapper():
#             print("登录.....")
#             fn()
#         return wrapper
# @auto_chain
# def sendMsg1():
#     print("发送消息1111")
# @auto_chain
# def sendMsg2():
#     print("发送消息2222")
#
# sendMsg1()
# sendMsg2()


# 语法糖装饰器嵌套
# print('\n')
# def auto_chain(checkInFn):
#     def loginWrapper(loginFn):
#         def wrapper():
#             print("开始注册")
#             loginFn(checkInFn)
#         return wrapper
#     return loginWrapper
# def checkIn():
#     print("自动打卡")
# @auto_chain(checkIn)  # 这里传入打卡函数
# def login(checkInFn):
#     print("自动登录")
#     checkInFn()
#
# login()


