


### 元组
print("=============Tuple=============")
t = (1, 2, 2, 3, 4, 4, 5)
print("t.count(4) = ", t.count(4))   # 2
print("t.index(3) = ", t.index(1))   # 1 的索引是 0
print("t.index(5) = ", t.index(5))   # 5 的索引是 6
print("type(t) = ",type(t),"\n")
# 元组同样支持切片操作
print("t[1:] = ", t[1:], "\n")
print("len(t) = ", len(t), "\n")

# 解包
t1 = (1,2,3)
a,b,c = t1;
print("a, b, c = ", a, b, c,"\n\n\n")


### 字典
print("=============Dict=============")
d = {'a': 1, 'b': 2}
print("type(d) = ", type(d), "\n")

print("d.get('a') = ", d.get('a'), "\n")              # 1
print("d.get('z', 0) = ", d.get('z', 0), "\n")           # 0

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

print("d.items() = ", d.items(), "\n")

d.update({'c': 3})
print("d = ", d, "\n")

v = d.pop('b')                 # 移除 b
print("v = ", v, "\n")

d.setdefault('d', 4)           # 添加 d: 4
print("d = ", d, "\n")

d.clear()
print("d = ", d, "\n")                       # {}



### 集合
print("=============Set=============")
# 空集合要用 set()
s = set()

# 有元素的集合
s = {1, 2, 3, 3, 2}
print(s)  # {1, 2, 3}，自动去重
s = {1, 2, 3}
s.add(4)
s.remove(1)
s.update({5,6,7})
print("s = ", s, "\n")
print(2 in s, "\n")

# 集合运算
a = {1, 2, 3}
b = {2, 3, 4}

print("a & b = ", a & b, "\n")  # {2, 3} 交集
print("a | b = ", a | b, "\n")  # {1, 2, 3, 4} 并集
print("a - b = ", a - b, "\n")  # {1} 差集
print("a ^ b = ", a ^ b, "\n")  # {1, 4} 对称差集












