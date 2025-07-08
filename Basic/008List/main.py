



fruits = ['apple', 'banana', 'cherry']

numbers = [1, 2, 3, 4, 5]

mixed = [1, 'hello', True, 3.14]

print(type(fruits))

# 常用操作
print(fruits[0])         # 访问元素
fruits[1] = 'pear'       # 修改元素
fruits.append('grape')   # 添加元素
del fruits[0]            # 删除元素
print(len(fruits))       # 列表长度
print('pear' in fruits)  # 成员判断
print(fruits)

# 常用方法
lst = [1, 2, 3]
lst.append(4)           # [1, 2, 3, 4]
lst.insert(1, 100)      # [1, 100, 2, 3, 4]
lst.extend([5, 6])      # [1, 100, 2, 3, 4, 5, 6]
lst.remove(100)         # [1, 2, 3, 4, 5, 6]
last = lst.pop()        # 6 被弹出
lst.sort()              # 升序排列
lst.reverse()           # 反转顺序
copy_lst = lst.copy()   # 拷贝一份
print("copy_lst = ",copy_lst, "\n")

# 列表推导式
evens = []
# 方式一
# evens = [x for x in range(10) if x % 2 == 0]
# 方式二
[evens.append(x) for x in range(10) if x % 2 == 0]

print("evens = ", evens, "\n")

[print(fruit) for fruit in fruits]
