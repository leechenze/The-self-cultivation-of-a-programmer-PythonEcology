


## __new__ 实例构造器
# class Demo:
#     def __new__(cls, *args, **kwargs):
#         print("执行 __new__：分配内存空间")
#         instance = super().__new__(cls)
#         print("instance: ", instance)
#         return instance
#
#     def __init__(self, name):
#         print("执行 __init__：初始化对象属性")
#         self.name = name
#
#
# obj = Demo("Lee")
# print(f"对象创建完成：{obj.name}")
# print("obj: ", obj)





# 单例模式
# class Singleton(object):
#     obj = None
#     def __new__(cls, *args, **kwargs):
#         print('singleton 的 __new__')
#         if cls.obj == None:
#             cls.obj = super().__new__(cls)
#         return cls.obj
#     def __init__(self):
#         print('singleton 的 __init__')
#
# s1 = Singleton()
# print('s1: ', s1)
#
# s2 = Singleton()
# print('s2: ', s2)






### 魔法方法
## __doc__
## 输出模块,类,函数的文档说明('''描述文档用三引号''')
# class Person:
#     '''人类的描述信息'''
#     pass
# person = Person()
# print(Person.__doc__)
# print(person.__doc__)


## __module__
## 表示当前操作对象所在的模块
## __class__
## 表示当前操作对象所在的类
# class B:
#     def func(self):
#         print('哈哈哈')
# b = B()
# print(b.__class__)
# print(b.__module__)



## __str__
## 改变实例对象的字符串的返回值, __new__也可以
# class A:
#     def __str__(self):
#         return "魔法方法__str__重写返回值"
# a = A()
# print(a)





## __call__
## 使实例对象成为可调用的对象, 像函数那样调用, 实例对象的调用结果就是call的返回值
## callable() 判断对象是否是可调用对象
# class A:
#     def __call__(self, *args, **kwargs):
#         return "自定义call方法"
# a = A()
# print(a())























