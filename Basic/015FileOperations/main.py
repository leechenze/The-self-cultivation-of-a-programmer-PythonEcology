


### 基础操作
# file = open('text.txt', 'a+')
#
# print('file.name = ', file.name)
# print('file.mode = ', file.mode)
# print('file.closed = ', file.closed)


### 读写操作
# print('\n')
# print('file = ', file)

# print('file.read() = ', file.read())
## 重置指针到开头
# file.seek(0)
# print('file.read(5) = ', file.read(5))

# print('file.readline() = ', file.readline())
# print('file.readline() = ', file.readline())


## readline
# while True:
#     con = file.readline()
#     if not con:
#         break
#     print('con = ', con)


## readlines
# con = file.readlines()
# print('con = ', con)
# for i in con:
#     print('i = ', i)



## write和tell和seek
# file.write("lalala")
# print('file.tell() = ', file.tell())
# file.seek(0)
# print('file.tell() = ', file.tell())
#
# # seek之后才能读取到 read 内容, 或者改变open方法的第二个参数为只读访问模式也可以读到
# print('file.read() = ', file.read())



# # 关闭文件
# file.close()
# print('file.closed = ', file.closed)






### with关键字
## with open(name)作用就是代码执行完, 系统会自动调用close函数, 省略关闭文件的步骤
# with open('text1.txt','w') as file:
#     file.write('emmmmm......')
#     print('file.closed = ', file.closed)
# print('file.closed = ', file.closed)






















