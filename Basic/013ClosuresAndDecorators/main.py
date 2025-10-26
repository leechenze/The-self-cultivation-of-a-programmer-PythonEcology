


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
    return fibonacci(n-2) + fibonacci(n-1)
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
def test():
    print("开始注册")
    print("登录")
test()

















