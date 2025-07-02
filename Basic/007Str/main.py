



# str和bytes之间的转换(编码和解码)
s = 'hello world'
print(s, type(s))
print('\n')


b = s.encode('utf-8')
print(b, type(b))
print('\n')

s1 = b.decode('utf-8')
print(s1, type(s1))
print('\n')

# Str常用操作
# 运算符操作
print("Hi" + "there", "\n")
print("Hi" * 3, "\n")
print("py" in "python", '\n')
print("ba" not in "python", '\n')
print("cat" < "dog", '\n')        # True（字典序比较）
# 字符串常见操作
s = "abcdef"
print(s[0], '\n')     # a
print(s[-1], '\n')    # f
print(s[1:4], '\n')   # bcd
print(s[::2], '\n')   # ace（每隔1个取1个）
print(s[::3], '\n')   # ad（每隔2个取1个）
# 获取长度
print(len(s1), '\n')
# 查找子串
s = 'hello world'
print(s.find('world'), '\n')
print(s.find('python'), '\n')
print(s.count('l'), '\n')
# 替换字符串
s = "I like Java"
print(s.replace("Java", "Python"), '\n')
# 转换大小写
s = 'hello world'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title(), '\n')
# 内容判断
s = "abc123"
s1 = 'abc'
s2 = '123'
print(s.isalpha())   # False（含数字）
print(s.isdigit())   # False（含字母）
print(s.isalnum())   # True（字母数字）
print("   ".isspace())  # True（全是空格）
# 去除空白
s = "  hello  "
print(s.strip())   # "hello"
print(s.lstrip())  # "hello  "
print(s.rstrip())  # "  hello"
# 拆分与连接
s = "a,b,c"
print(s.split(","))            # ['a', 'b', 'c']
print("-".join(['1', '2']))    # '1-2'















