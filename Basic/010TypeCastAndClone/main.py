
import copy

### 类型转换
print("=============类型转换=============")
num = 1.2
print(type(num))
# 浮点型强转为整型会去掉小数部分, 只保留整数部分
print(int(num))

str0 = '10'
str1 = '-10'
str2 = 'anglee'

print(int(str1))
print(float(11))
print(str(12), type(str(12)))
print(str(12.00000))
print(str(12.00001))
print(str([1,2,3]))
print(eval("10 + 20"))
print(list({'name':'anglee','age':20}))



# 用户从控制台输入, 判断年龄
# input默认输入是字符串类型
# age = int(input("请输入年龄"))
# print(type(age))
# if age >= 18:
#     print("已成年")
# else:
#     print("未成年")



### 深浅拷贝
print('\n')
print("=============深浅拷贝=============")
# 浅拷贝
# 创建新的对象, 拷贝第一层的数据, 嵌套层会指向原来的地址

list0 = [1,2,3,[1,2,3],4]
list1 = copy.copy(list0)
list0.append(5)

print('list0',list0)
print('list1',list1)
print('list0[3]的内存地址是: ', id(list0[3]))
print('list1[3]的内存地址是: ', id(list1[3]))

list0[3].append(4)
print('list0[3]',list0[3])
print('list1[3]',list1[3])

# 深拷贝
list2 = [1,2,3,[1,2,3],4]
list3 = copy.deepcopy(list2)
list2[3].append(4)
print('list2',list2)
print('list3',list3)
print('list2[3]',list2[3])
print('list3[3]',list3[3])


### 可变与不可变对象
# 可变对象
print('\n')
list4 = [1,2,3,4]
print("list4的内存地址: ", id(list4))
list4.append(5)
print("list4", list4)
print("list4的现内存地址", id(list4))

# 不可变对象
print('\n')
num1 = 10
print("num1的内存地址是: ", id(num1))
num1 = 15
print("num1修改后的内存地址是: ", id(num1))

### 所以深浅拷贝只针对可变对象, 不可变对象没有拷贝的说法




