






# 数值类型
# 布尔值
print(type(True))
print(True + True)
print("\n")

# 复数值
z = 3 + 4j      # complex 类型
print(z.real)   # 实部 3.0
print(z.imag)   # 虚部 4.0
print("\n")

# 字符串
name = "douglas"
name = 'anglee'
# 多行字符串
name = '''
douglas
ang
lee
'''
name = """
douglas
ang
lee
"""
print(name)
print('\n')

# 格式化输出
# % 占位符
name = "douglas"
age = 25
print("My name is %s and I am %d years old." % (name, age))
# str.format() 格式化
name = "douglas"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0}, age is {1}".format("Tom", 20))
print("My name is {name}, age is {age}".format(name="Tom", age=20))
# f-string 格式化
name = "Eve"
age = 22
print(f"My name is {name} and I am {age} years old.")









