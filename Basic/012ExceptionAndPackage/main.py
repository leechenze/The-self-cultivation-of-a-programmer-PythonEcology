
import sys
import cus_module
from cus_module import *
from py_pkg01 import *
# from py_pkg01 import register,login

### 抛出异常
# def func0():
#     print("嘿嘿嘿")
#     raise Exception('anglee 抛出异常');
#     print("哈哈哈哈哈")
# func0()

# 密码长度不足时抛出异常, 并捕获异常
# def login():
#     pwd = input("请输入您的密码: \n")
#     if len(pwd) >= 6:
#         return '密码输入成功'
#     else:
#         raise Exception("长度不足6位数, 密码输入失败")

# try:
#     print(login())
# except Exception as e:
#     print(e)


### 模块
# 自定义模块
cus_module.funcA()
funcB()
print(cus_module.name)


print(__name__)
print("name:", __name__)
print("file:", __file__)
print("package:", __package__)
print("loader:", __loader__)
print("spec:", __spec__)





### 包
print('\n')
register.reg()
login.login()














