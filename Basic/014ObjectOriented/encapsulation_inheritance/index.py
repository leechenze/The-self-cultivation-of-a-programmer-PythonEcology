

# 隐藏属性/方法
# class Person:
#     name = 'anglee'
#     __age = 30
#     def introduce(self):
#         return f'{self.name}的年龄是{self.__age}'
#     def __having_an_affair(self):
#         return f'{self.name}和hillary...having an affair'
# p = Person()
# print(p.name)
# # print(p.__age)
# print(p._Person__age)
# print(p.introduce())
# print(p._Person__having_an_affair())




# 私有属性/方法
# class Person:
#     name = 'anglee'
#     __age = 30
#     _sex = 'man'
#     def introduce(self):
#         return f'{self.name}的年龄是{self.__age}, 性别是{self._sex}'
#     def _bad_habits(self):
#         return f'{self.name}的年龄是{self.__age}, 坏习惯是抽烟喝酒'
# p = Person()
# print(p._sex)
# print(p._bad_habits())







# 继承
# class Person:
#     def eat(self):
#         print("eating...")
#     def sing(self):
#         print('singing...')
# class Girl(Person):
#     pass
# girl = Girl()
# girl.eat()







# 父类方法重写
# class Father:
#     def money(self):
#         print('一百万可以被继承')
# class Son(Father):
#     def money(self):
#         # Father.money(self)
#         # super(Son, self).money()
#         # 可以简写为 super().money()
#         print('自己赚一千万')
# son = Son()
# son.money()







# 多继承
# class Father(object):
#     def money(self):
#         print('爸爸拥有亿万资产')
# class Mather(object):
#     def money(self):
#         print('妈妈拥有百万资产')
#     def appearance(self):
#         print('妈妈拥有绝世容颜')
#
# class Son(Father, Mather):
#     pass
#
# son = Son()
# son.money()
# son.appearance()
# print(Son.__mro__)





# 静态方法
# class Person:
#     @staticmethod
#     def study():
#         print('人类会学习')


# 类方法
# class Person:
#     species = 'Homo sapiens'
#     def __init__(self, name):
#         self.name = name
#     @classmethod
#     def from_fullname(cls, fullname):
#         # cls 是调用时的类（支持子类覆盖）
#         first = fullname.split()[0]
#         return cls(first)
# class Student(Person):
#     pass
# p = Person.from_fullname("Alice Smith")
# s = Student.from_fullname("Bob Lee")
#
# print(p.name)
# print(s.name)
# print('Alice Smith'.split())











