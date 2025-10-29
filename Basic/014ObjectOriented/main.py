

# 类定义
# class Washer:
#     height=800
#     def wash(self):
#         print("我会洗衣服")
#
# Washer.width = 450





# 创建对象
# wa = Washer()
# print(wa)
# wa.wash()


# 实例属性
# class Person:
#     name = 'anglee'
#     def introduce(self):
#         print(f'{Person.name}:{self.age}')
#
# person = Person()
# person.age = 18
# person.sex = 'man'
# person.introduce()
#
# person2 = Person()
# print(person2.name)
# 访问不到, 因为 sex 是person实例私有设置的, 而不是Person类的
# print(person2.sex)






# 构造函数
# class Person:
#     def __init__(self,name,age,height):
#         print('这是Person __init__ 方法, 初始化会调用')
#         self.name = 'douglas'
#         self.age = 18
#         self.height = 180
#     def play(self):
#         print(f'{self.name}在打游戏')
#     def introduce(self):
#         print(f'{self.name}的年龄是{self.age},身高是{self.height}')
#
#
# person = Person("anglee", 18,196)
# person.play()
# person.introduce()







# 析构函数
# class Person:
#     def __del__(self):
#         print("对象销毁了")
# p = Person()
# del p
# print("最后一行输出")





# 封装和继承(encapsulation_inheritance)
# 单例模式和魔法方法(single_pattern_magic_method)










