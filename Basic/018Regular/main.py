import re


### match, 从字符串开头匹配, 返回 Match 对象 或 None
# m = re.match(r'\d+','123abc')
# print(m.group())  # 123


### search, 搜索整个字符串, 找到第一个匹配
# s = re.search(r'\d+', 'abc123def')
# print(s.group())  # 123


### findall, 返回所有匹配的 列表
# f = re.findall(r'\d+', 'a1b2c3')
# print(f)  # ['1', '2', '3']


### finditer, 返回 迭代器, 每个元素是 Match 对象
# it = re.finditer(r'\d+', 'a1b2c3')
# print(it)
# for match in it:
#     print(match.group())
# 输出：
# 1
# 2
# 3


### sub, 替换匹配的字符串
# s = re.sub(r'\d+', '#', 'a1b2c3')
# print(s)  # a#b#c#


### split, 按正则分割字符串
# s = re.split(r'\d+', 'a1b2c3')
# print(s)  # ['a', 'b', 'c', '']


### compile, 编译正则, 返回 Pattern 对象, 可重复使用
# pattern = re.compile(r'\d+')
# print(pattern.findall('a1b2c3'))  # ['1','2','3']



