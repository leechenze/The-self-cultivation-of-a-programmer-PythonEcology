

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
class Person:
    name = 'anglee'
    __age = 30
    _sex = 'man'
    def introduce(self):
        return f'{self.name}的年龄是{self.__age}, 性别是{self._sex}'
    def _bad_habits(self):
        return f'{self.name}的年龄是{self.__age}, 坏习惯是抽烟喝酒'
p = Person()
print(p._sex)
print(p._bad_habits())



