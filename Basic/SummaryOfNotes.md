博学之, 审问之, 慎思之, 明辨之, 笃行之;
零、壹、贰、叁、肆、伍、陆、柒、捌、玖、拾;



零.初识Python
    
    Python 是一种高级、通用、解释型、动态类型的编程语言,具有简洁优雅、易读易写、功能强大等特点. 
    它支持面向对象、过程式编程和函数式编程范式,是目前最流行的编程语言之一,广泛应用于Web 开发、数据分析、人工智能、自动化运维、科学计算等领域. 
    
    Python 由**荷兰程序员 Guido van Rossum（吉多·范罗苏姆）**于 1989 年圣诞节期间在阿姆斯特丹开发,并于 1991 年正式发布了第一个公开版本（Python 0.9.0）. 
    Guido 的设计理念是让语言“像人类语言一样清晰易懂”, 因此 Python 特别注重代码的可读性.
    
    目前 Python 拥有两个主要版本系列: 
        Python 2.x: 已于 2020 年 1 月正式停止支持（EOL）,不再维护.
        Python 3.x: 当前主流版本,推荐学习和开发使用. 
    




壹.注释和输出函数(helloPython.py)
    
    print函数参数
        *values
            可以设定多个
        sep
            指定间隔符, 用来间隔多个对象, 默认值是一个空格
        end
            用来设定以什么结尾, 默认是 \n 换行符
    
    # 单行注释
        
    """
        多行注释
    """
    
    '''
        多行注释
    '''



贰.变量和标识符(002VariablesAndIdentifiers)

    变量
        特点：
            变量绑定对象，类型由对象决定。
        常见的数据类型：
            | 类型名称       | 示例                  | 说明                |
            | ---------- | ------------------- | ----------------- |
            | `int`      | `x = 10`            | 整数类型              |
            | `float`    | `pi = 3.14`         | 浮点数类型             |
            | `str`      | `name = "Alice"`    | 字符串类型             |
            | `bool`     | `flag = True`       | 布尔值（True / False） |
            | `list`     | `nums = [1, 2, 3]`  | 列表                |
            | `tuple`    | `pos = (1, 2)`      | 元组（不可变序列）         |
            | `dict`     | `user = {"id": 1}`  | 字典（键值对）           |
            | `set`      | `tags = {"a", "b"}` | 集合（无序不重复）         |
            | `NoneType` | `val = None`        | 空值类型              |
        
    标识符
        | 规则                       | 示例                                  |
        | ------------------------- | ----------------------------------- |
        | 只能由字母、数字、下划线组成      | `user1`, `my_name`, `_temp`         |
        | **不能以数字开头**           | `1user` ❌ 不合法                       |
        | **不能是 Python 的关键字**   | `class`, `if` ❌ 不合法                 |
        | 区分大小写                   | `age` 和 `Age` 是不同变量                 |
        | 通常遵循命名风格（推荐）       | 小写字母 + 下划线，如 `user_id`、`get_name()` |
        命名规范：
            见名知义
            下划线分割
            大驼峰命名
            小驼峰命名

        

叁.数值类型和字符串(003NumberAndStr)
    
    数值类型：
        int
        float
        bool
            布尔可以当作整型对待，True = 1，false = 0。
            比如：
                True + True = 2
                True + 1 = 2
        complex
            j是虚数关键字/关键单位。
    字符串：
        单双引号都可以，多行用三引号
    格式化输出：
        占位符的三种方式：
            1.%
            2.str.format()
            3.f"{变量名}"



肆.运算符与转义字符(004OperatorsAndEscapeCharacter)
    
    运算符
        算术运算符（Arithmetic Operators）
            | 运算符  | 含义     | 示例       | 结果    |
            | ---- | ------ | -------- | ----- |
            | `+`  | 加法     | `3 + 2`  | `5`   |
            | `-`  | 减法     | `3 - 2`  | `1`   |
            | `*`  | 乘法     | `3 * 2`  | `6`   |
            | `/`  | 除法（浮点） | `3 / 2`  | `1.5` |
            | `//` | 整除     | `3 // 2` | `1`   |
            | `%`  | 取模     | `3 % 2`  | `1`   |
            | `**` | 幂运算    | `2 ** 3` | `8`   |
        比较运算符（Comparison Operators）
            | 运算符  | 含义   | 示例       | 结果      |
            | ---- | ---- | -------- | ------- |
            | `==` | 等于   | `3 == 2` | `False` |
            | `!=` | 不等于  | `3 != 2` | `True`  |
            | `>`  | 大于   | `3 > 2`  | `True`  |
            | `<`  | 小于   | `3 < 2`  | `False` |
            | `>=` | 大于等于 | `3 >= 3` | `True`  |
            | `<=` | 小于等于 | `2 <= 3` | `True`  |
        赋值运算符（Assignment Operators）
            | 运算符   | 含义    | 示例        | 等价于          |
            | ----- | ----- | --------- | ------------ |
            | `=`   | 赋值    | `x = 3`   |              |
            | `+=`  | 加后赋值  | `x += 2`  | `x = x + 2`  |
            | `-=`  | 减后赋值  | `x -= 2`  | `x = x - 2`  |
            | `*=`  | 乘后赋值  | `x *= 2`  | `x = x * 2`  |
            | `/=`  | 除后赋值  | `x /= 2`  | `x = x / 2`  |
            | `//=` | 整除后赋值 | `x //= 2` | `x = x // 2` |
            | `%=`  | 取模后赋值 | `x %= 2`  | `x = x % 2`  |
            | `**=` | 幂后赋值  | `x **= 2` | `x = x ** 2` |
        逻辑运算符（Logical Operators）
            | 运算符   | 含义 | 示例               | 结果      |
            | ----- | -- | ---------------- | ------- |
            | `and` | 与  | `True and False` | `False` |
            | `or`  | 或  | `True or False`  | `True`  |
            | `not` | 非  | `not True`       | `False` |
        位运算符（Bitwise Operators）
            | 运算符  | 含义   | 示例       | 结果   |     |     |
            | ---- | ---- | -------- | ---- | --- | --- |
            | `&`  | 按位与  | `5 & 3`  | `1`  |     |     |
            | \`   | \`   | 按位或      | \`5  | 3\` | `7` |
            | `^`  | 按位异或 | `5 ^ 3`  | `6`  |     |     |
            | `~`  | 按位取反 | `~5`     | `-6` |     |     |
            | `<<` | 左移   | `5 << 1` | `10` |     |     |
            | `>>` | 右移   | `5 >> 1` | `2`  |     |     |
        成员运算符（Membership Operators）
            | 运算符      | 含义      | 示例                 | 结果     |
            | -------- | ------- | ------------------ | ------ |
            | `in`     | 是否在序列中  | `'a' in 'abc'`     | `True` |
            | `not in` | 是否不在序列中 | `'d' not in 'abc'` | `True` |
        身份运算符（Identity Operators）
            | 运算符      | 含义         | 示例           | 结果           |
            | -------- | ---------- | ------------ | ------------ |
            | `is`     | 判断是否引用同一对象 | `x is y`     | `True/False` |
            | `is not` | 判断是否非同一对象  | `x is not y` | `True/False` |
    输入函数
        input(prompt)
            prompt：可选参数，表示提示用户输入的字符串。
        name = input("请输入你的名字：")
        print("你好，" + name)
    转义字符
        | 转义字符         | 含义            | 示例/说明                              |
        | ------------ | ------------- | ---------------------------------- |
        | `\\`         | 反斜杠           | `'\\'` → `'\'`                     |
        | `\'`         | 单引号           | `'It\'s ok'`                       |
        | `\"`         | 双引号           | `"He said \"Hi\""`                 |
        | `\n`         | 换行            | `"hello\nworld"`                   |
        | `\r`         | 回车（回到行首）      | `"hello\rworld"` → `worldo`        |
        | `\t`         | 水平制表符（Tab）    | `"hello\tworld"`                   |
        | `\b`         | 退格（backspace） | `"abc\b"` → `'ab'`                 |
        | `\f`         | 换页（form feed） | 很少用，一般在打印机或终端模拟中                   |
        | `\v`         | 垂直制表符         | 很少用                                |
        | `\a`         | 响铃（alert）     | 控制台响一声（取决于环境）                      |
        | `\0`         | 空字符（null）     | 用于表示字符结束（某些底层结构）                   |
        | `\ooo`       | 八进制字符         | `\141` → `'a'`                     |
        | `\xhh`       | 十六进制字符        | `\x61` → `'a'`                     |
        | `\N{name}`   | Unicode 字符名   | `\N{LATIN SMALL LETTER A}` → `'a'` |
        | `\uXXXX`     | Unicode（4位）   | `\u4F60` → `'你'`                   |
        | `\UXXXXXXXX` | Unicode（8位）   | `\U00004F60` → `'你'`               |
    


伍.逻辑判断语句(005IfLogicalJudgmentStatement)
    
    除了 0、0.0、空字符串、空列表、空字典、None 等“被认为是 False 的值”以外，
    其他任何值在布尔上下文中都被认为是 True。
    
    关键字: 
        if elif else
    三元表达式语法: 
        <表达式> if <条件> else <表达式>
        示例: 
            print('b大') if a < b else print('a大')
            res = 'b大' if a < b else 'a大'


陆.For和While循环(006ForAndWhileLoop)

    Python中没有经典的三段式计数For循环
    循环可用于遍历序列（如列表、字符串、元组、字典等）或其他可迭代对象。
    
    range参数：
        | 参数      | 说明                |
        | ------- | ----------------- |
        | `start` | 起始值（默认是 0）        |
        | `stop`  | 终止值（**不包含 stop**） |
        | `step`  | 步长（默认是 1，可为负数，为负数时就是倒叙）    |
        示例：
            for i in range(1, 10, 1):
                输出 1 - 10
            for i in range(1, 10, 2):
                输出 1，3，5，7，9
            for i in range(10, 0, -1):
                输出：10 9 8 ... 1
    break：跳出当前循环
    continue：跳过本次循环，进入下一次循环



柒.字符串(007Str)
    
    字符串编码
        str.encode('utf-8') 类型将转换为 bytes
        bytes.decode('utf-8') 类型将转换为 str
    常见操作
        运算符操作
            | 运算符         | 功能说明          | 示例代码                   | 输出              |
            | ----------- | ------------- | ---------------------- | --------------- |
            | `+`         | 字符串拼接         | `"Hello, " + "world!"` | `Hello, world!` |
            | `*`         | 重复字符串         | `"Hi! " * 3`           | `Hi! Hi! Hi! `  |
            | `in`        | 成员包含判断        | `"a" in "apple"`       | `True`          |
            | `not in`    | 判断不包含         | `"z" not in "apple"`   | `True`          |
            | `==`        | 相等比较          | `"abc" == "abc"`       | `True`          |
            | `!=`        | 不等比较          | `"abc" != "ABC"`       | `True`          |
            | `< > <= >=` | 字符串大小比较（按字典序） | `"apple" < "banana"`   | `True`          |
        常用方法
            | 方法               | 说明           | 示例和返回值                                    |
            | ---------------- | ------------ | ----------------------------------------- |
            | `s.upper()`      | 转大写          | `"abc".upper()` → `"ABC"`                 |
            | `s.lower()`      | 转小写          | `"ABC".lower()` → `"abc"`                 |
            | `s.capitalize()` | 首字母大写        | `"hello".capitalize()` → `"Hello"`        |
            | `s.title()`      | 所有单词首字母大写    | `"hello world".title()` → `"Hello World"` |
            | `s.strip()`      | 去除首尾空格       | `"  hi  ".strip()` → `"hi"`               |
            | `s.lstrip()`     | 去除左边空格       | `"  hi".lstrip()` → `"hi"`                |
            | `s.rstrip()`     | 去除右边空格       | `"hi  ".rstrip()` → `"hi"`                |
            | `s.find(sub)`    | 查找子串首次出现位置   | `"abcabc".find("b")` → `1`                |
            | `s.index(sub)`   | 和find一样，但找不到时会抛错   | `"abcabc".index("b")` → `1`                |
            | `s.count(sub)`   | 返回字符出现的次数   | `"abcabc".count("b")` → `2`                |
            | `s.replace(a,b)` | 替换子串         | `"1+1=2".replace("1", "一")` → `"一+一=2"`   |
            | `s.split(sep)`   | 拆分成列表        | `"a,b,c".split(",")` → `['a','b','c']`    |
            | `sep.join(lst)`  | 用 sep 连接列表元素 | `"-".join(['a','b'])` → `"a-b"`           |
            | `s.isdigit()`    | 是否全是数字       | `"123".isdigit()` → `True`                |
            | `s.isalpha()`    | 是否全是字母       | `"abc".isalpha()` → `True`                |
            | `s.isalnum()`    | 是否全是字母或数字    | `"abc123".isalnum()` → `True`             |
            | `s.isspace()`    | 是否全是空白       | `"   ".isspace()` → `True`                |
            | `len(s)`         | 字符串长度        | `len("hello")` → `5`                      |
        ::切片语法案例示例
            | 切片语法        | 作用说明              | 结果（s="abcdefg") |
            | ----------- | ----------------- | --------------- |
            | `s[::1]`    | 正常顺序              | `'abcdefg'`     |
            | `s[::2]`    | 每隔1个字符取一个         | `'aceg'`        |
            | `s[1::2]`   | 从索引1开始，每2个取一个     | `'bdf'`         |
            | `s[::-1]`   | 倒序                | `'gfedcba'`     |
            | `s[1:6:2]`  | 从索引1到5，每2个取一个     | `'bd'`          |
            | `s[6:1:-1]` | 从索引6到2（不含2），反向取字符 | `'gfedc'`       |
        ::缺省时的默认值
            | 方向 | 表达式形式              | start 默认值  | stop 默认值      | step 默认值 | 整体效果描述                  |
            | -- | ------------------ | ---------- | ------------- | -------- | ----------------------- |
            | 正向 | `s[start:stop]`    | `0`        | `len(s)`      | `1`      | 从前往后依次取                 |
            | 正向 | `s[::step]`        | `0`        | `len(s)`      | 指定的值     | 从头开始，每隔 `step` 个取一个     |
            | 正向 | `s[start::step]`   | 指定         | `len(s)`      | 指定的值     | 从 `start` 开始，到结尾跳着取     |
            | 正向 | `s[:stop:step]`    | `0`        | 指定            | 指定的值     | 从头开始，到 `stop` 前跳着取      |
            | 正向 | `s[start:stop:]`   | 指定         | 指定            | `1`      | 正常切片，但没有跳步              |
            | 反向 | `s[::-1]`          | 最后一位      | `None`（切到头为止） | `-1`     | 整个字符串反转                 |
            | 反向 | `s[start::-1]`     | 指定         | `None`（切到头为止） | `-1`     | 从 `start` 反向一个个取到开头     |
            | 反向 | `s[start:stop:-1]` | 指定         | 指定            | `-1`     | 从 `start` 反向切到 `stop+1` |



捌.列表(008List)

    列表（List）是 Python 中最常用的数据结构之一，用来有序地存储一组元素，可以是任何类型，支持修改。
    常用操作
        | 操作名称     | 示例说明                            | 示例代码                                |
        | --------    | ------------------------------- | ----------------------------------- |
        | 访问元素     | 使用索引 `list[index]`              | `fruits[0]` → `'apple'`             |
        | 修改元素     | 使用 `list[index] = value`        | `fruits[1] = 'pear'`                |
        | 添加元素     | 使用 `append()` 或 `insert()`      | `fruits.append('grape')`            |
        | 删除元素     | 使用 `del` / `remove()` / `pop()` | `del fruits[0]`                     |
        | 列表长度     | 使用 `len(list)`                  | `len(fruits)`                       |
        | 检查元素是否存在 | 使用 `in` / `not in`              | `'apple' in fruits`                 |
        | 列表拼接     | 使用 `+` 或 `extend()`             | `list1 + list2`                     |
        | 列表重复     | 使用 `*`                          | `[1, 2] * 3` → `[1, 2, 1, 2, 1, 2]` |
        | 列表切片     | `list[start:end:step]`          | `fruits[0:2]`                       |
    常用方法
        | 方法             | 功能简述           | 示例代码                |
        | -------------- | -------------- | ------------------- |
        | `append(x)`    | 末尾添加一个元素       | `lst.append(10)`    |
        | `insert(i, x)` | 指定位置插入元素       | `lst.insert(1, 20)` |
        | `extend(iter)` | 扩展另一个序列/可迭代对象  | `lst.extend([3,4])` |
        | `remove(x)`    | 移除第一个匹配项       | `lst.remove(10)`    |
        | `pop([i])`     | 弹出并返回索引元素，默认最后 | `lst.pop()`         |
        | `clear()`      | 清空列表           | `lst.clear()`       |
        | `index(x)`     | 返回第一次出现的索引位置   | `lst.index(3)`      |
        | `count(x)`     | 统计某值出现次数       | `lst.count(2)`      |
        | `sort()`       | 就地排序（默认升序）     | `lst.sort()`        |
        | `reverse()`    | 反转列表顺序         | `lst.reverse()`     |
        | `copy()`       | 浅拷贝列表          | `lst2 = lst.copy()` |
    数组也同样支持[::]的切片语法
    列表推导式
        [表达式 for 变量 in 可迭代对象 if 条件]



玖.元组和字典和集合(009TupleAndDictAndSet)
    
    元组，是不可变的序列类型（不能增删改，只能读），用小括号 () 定义，元素可为任意类型。
    元组常见操作
        | 操作    | 示例代码              | 说明             |
        | ----- | ----------------- | -------------- |
        | 创建元组  | `t = (1, 2, 3)`   | 定义元组          |
        | 单元素元组 | `t = (1,)`        | **必须加逗号**才能是元组 |
        | 访问元素  | `t[0]`            | 索引访问           |
        | 切片    | `t[1:]`           | 取出一部分元素        |
        | 长度    | `len(t)`          | 元素个数           |
        | 成员判断  | `1 in t`          | 判断元素是否存在       |
        | 解包    | `a, b, c = t`     | 将元组解包成多个变量     |
        | 嵌套    | `t = (1, (2, 3))` | 元组内嵌套元组        |
    
    字典，只是称呼不同，在js中称为object，在java中是map，在python中称为dict即字典。
    字典常见操作
        | 操作      | 示例代码                     | 说明        |
        | ------- | ------------------------ | --------- |
        | 创建字典    | `d = {'a': 1, 'b': 2}`   | 使用花括号     |
        | 访问值     | `d['a']`                 | 通过键访问值    |
        | 修改值     | `d['a'] = 10`            | 如果键存在则修改  |
        | 添加键值对   | `d['c'] = 3`             | 如果键不存在则添加 |
        | 删除键值对   | `del d['a']`             | 删除指定键     |
        | 获取长度    | `len(d)`                 | 键值对数量     |
        | 判断键是否存在 | `'a' in d`               | 只查键，不查值   |
        | 遍历字典    | `for k, v in d.items():` | 同时遍历键和值   |
    字典常用方法
        | 方法                   | 用法                     | 说明             |
        | -------------------- | ---------------------- | -------------- |
        | `get(key, default)`  | `d.get('a', 0)`        | 安全获取键，不存在返回默认值 |
        | `keys()`             | `d.keys()`             | 获取所有键          |
        | `values()`           | `d.values()`           | 获取所有值          |
        | `items()`            | `d.items()`            | 获取键值对元组        |
        | `pop(key)`           | `d.pop('a')`           | 移除键并返回其值       |
        | `popitem()`          | `d.popitem()`          | 移除并返回最后一个键值对   |
        | `clear()`            | `d.clear()`            | 清空字典           |
        | `update(other)`      | `d.update({'b': 2})`   | 合并另一个字典        |
        | `setdefault(k, def)` | `d.setdefault('z', 0)` | 若无此键则添加，返回其值   |
        | `copy()`             | `new = d.copy()`       | 浅拷贝            |
    
    集合，集合是一个无序、无重复元素的数据结构。使用花括号 {} 或 set() 定义。
        不支持索引访问（因为无序）。元素必须是可哈希的（不可变）。
    集合常见操作
        | 操作   | 示例代码             | 说明            |
        | ---- | ---------------- | ------------- |
        | 添加元素 | `s.add(4)`       | 添加一个元素        |
        | 移除元素 | `s.remove(2)`    | 移除指定元素，不存在时报错 |
        | 安全移除 | `s.discard(2)`   | 移除元素，不存在不报错   |
        | 清空集合 | `s.clear()`      | 清空所有元素        |
        | 复制集合 | `s2 = s.copy()`  | 浅拷贝           |
        | 集合长度 | `len(s)`         | 元素个数          |
        | 成员测试 | `3 in s`         | 判断是否存在        |
        | 遍历集合 | `for item in s:` | 集合是可迭代对象      |
    集合常用方法
        | 方法名             | 作用           |
        | --------------- | ------------ |
        | `add(elem)`     | 添加元素         |
        | `remove(elem)`  | 删除元素（不存在报错）  |
        | `discard(elem)` | 删除元素（不存在不报错） |
        | `clear()`       | 清空集合         |
        | `copy()`        | 浅拷贝          |
        | `pop()`         | 随机移除一个元素并返回它 |
        | `update(iter)`  | 批量添加（合并）元素   |
    集合运算(数学意义)
        | 运算   | 符号 / 方法                                 | 示例                    |         |
        | ---- | --------------------------------------- | --------------------- | ------- |
        | 交集   | `&` / `set1.intersection(set2)`         | 共同元素                  |         |
        | 并集   | `｜` / `set1.union(set2)`               | 所有不重复元素 |             |           |
        | 差集   | `-` / `set1.difference(set2)`           | 在 set1 中但不在 set2 中    |         |
        | 对称差集 | `^` / `set1.symmetric_difference(set2)` | 两者独有元素之合集             |         |
        | 子集判断 | `<=` / `issubset()`                     | set1 是否是 set2 的子集     |         |
        | 超集判断 | `>=` / `issuperset()`                   | set1 是否包含 set2        |         |



拾.类型转换和深浅拷贝(010TypeCastAndClone)
    
    类型转换
        int(x)
            将x转换为整数
        float(x)
            将x转换为浮点数
        str(x)
            将对象x转换为一个字符串
        eval(str)
            用于计算字符串中的有效Python表达式, 返回一个对象
        tuple(s)
            将序列s转换为元组
        list(s)
            将序列s转换为列表
        chr(x)
            将一个整数转换为字符
    
    深浅拷贝
    
    可变与不可变对象
        可变对象
            变量对应的值可以被修改, 但是内存地址不会发生改变, 这种数据是可变类型
            常见的可变类型
                列表      list
                字典      dict
                集合      set
        不可变对象
            变量对应的值不可以被修改, 一旦修改就会被分配新的内存空间.
            常见的不可变类型
                数值类型        int, bool, float, complex
                字符串          str
                元组            tuple
        





拾壹.函数(011Function)
    
    基本格式:
        def funcName(params):
            funcBody
            return returnVal;
    无返回值时返回None, 有多个返回值时会打包成一个元组(tuple)
    函数参数分类
        必备参数
            即形参有几个, 实参就必须要有几个
        默认参数
            def func(a = 8)
                return a + 1
            如果没有传值, 将使用默认值执行函数
        可变参数
            def func(*args):
                print(args,type(args))
                print(args[1])
            func(1,2,'3')
            可变参数的接受值是一个元组类型
        关键字参数
            def func1(**kwargs):
                print(kwargs, type(kwargs))
            func1()
            func1(name='anglee',age = 20)
            关键字参数的接受值是一个元组类型, 也属于可变参数的一种
    
    函数嵌套
        即一个函数中包含另一个函数, 由缩进决定层级关系
        
        def study():
            print('learning in evening')
            def course():
                print('python base')
            course()
        study()
    

    作用域
        全局变量
            在函数外部定义的变量, 在整个python文件中都生效的
        局部变量
            在函数内部定义的变量, 只在函数内生效的变量.
            
        关键字
            global
                局部变量内使用全局变量时, 用global声明变量名, 就会变成全局变量
            nonlocal
                闭包内修改外层函数变量, 而非全局变量, 注意如果有多层嵌套函数时, 也仅仅会修改上一级的外层函数

            
    匿名函数lambda:
        格式:
            普通参数函数
                add = lambda a,b:a+b
            无参函数
                res = lambda : '无参匿名函数'
            可变参数
                func4 = lambda name,age = 18:(name,age)
                    (name,age)是因为函数有多个返回值时是元组的形式接收的.
            关键字参数
                func5 = lambda **kwargs:kwargs['name'] + '-' + str(kwargs['age'])
        结合三元表达式
            res = lambda a, b : 'b大' if a1<b1 else "a大"
        
    内置函数
        即python中已定义好的一些函数, 大些字母开头一般是内置常量名, 小写字母开头一般是内置函数名
        import builtins
        print(dir(builtins))
        常用内置函数
            set                             创建一个无序不重复的元素集
            list                            将一个可迭代对象转换为列表
            tuple                           将一个可迭代对象转换为元组
            abs                             返回绝对值
            sum                             将一个可迭代对象求和(字典除外)
            min                             求最小值
            max                             求最大值
            zip                             将一个可迭代对象中对应的元素打包成一个个元组
            map                             映射可迭代参数的那个元素
            reduce                          累计参数序列中的元素
        
        
    拆包/解包
        对于函数中的多个返回数据,去掉元组,列表或字典,直接获取里面的数据
        
        示例
            tup0 = (1,2,3,4)
            方法一
                a,b,c,d = tup0
            方法二
                *tup0(这种方式只在函数调用时的实参列表中使用)
            





拾贰.异常模块与包(012ExceptionAndPackage)
    
    模块
        一个py文件就是一个模块, 即导入一个模块本质上就是执行一个py文件
        模块分类
            内置模块
                random,time,os,logging....
            三方模块
                通过 pip install 模块名 下载得到的第三方模块
            自定义模块
                自己在项目中定义的模块, 注意自定义的模块不要与内置模块的命名其冲突
        导入模块
            import 模块名
            from ... import ... 从模块中导入指定部分
            from ... import *   从模块中导入所有部分(谨慎使用!)
            别名
                import cus_module as ctmd
                from cus_module import funcA as a, name, funcB as b
        内置全局变量
            | 变量名            | 含义                                   |
            | -------------- | ------------------------------------ |
            | `__file__`     | 模块的文件路径（例如 `/path/to/cus_module.py`） |
            | `__package__`  | 当前模块属于哪个包（如 `"mypackage.subpkg"`）    |
            | `__loader__`   | 加载此模块的加载器对象                          |
            | `__spec__`     | 模块的导入规范对象（包含元信息）                     |
            | `__doc__`      | 模块的文档字符串（模块顶层 docstring）             |
            | `__builtins__` | 当前模块可直接使用的内建命名空间                     |
            | `__cached__`   | `.pyc` 编译缓存文件的路径（仅对已编译模块存在）          |
            | `__name__`     | 用于          |
        
    包
        即项目结构中的文件夹目录
            与普通文件夹的区别, python包是默认有包含__int__.py的文件的.
        作用
            包就是将有联系的模块放在同一个文件夹下, 并且在这个文件夹中创建一个名字为__init__.py的文件.
            那么这个文件夹就称之为包, 有效避免模块名称冲突的问题, 让结构更清晰
        注意：
            一个py文件是一个模块,一个PythonPackage也是一个模块,当导入import这个包时,会默认执行__init__.py这个文件
            __init__.py文件不要写过多的代码, 保证内容简单
            __all__变量是一个列表, 可以控制要引入的东西(模块,函数,类等...)
            包的本质依然是模块, 包又可以包含包
            python3 -m mypkg  python3可以直接执行一个PythonPackage,前提是该包中有__main__.py文件, 并且初始化的__init__.py会比__main__.py先执行
        
            
        


拾叁.闭包和装饰器(013ClosuresAndDecorators)
    
    递归函数
        函数自己调用自己, 用于把大问题拆成小问题逐步求解

    闭包
        函数内部定义了另一个函数, 并且内部函数引用了外部函数的变量的函数
    
    装饰器
        解释
            装饰器本质上就是一个python函数, 它可以让其他函数在不需要做任何代码变动的前提下增加额外功能
            装饰器的返回值也是一个函数对象
            装饰器不修改原程序或函数的代码, 也不改变函数或程序调用方法
    
        闭包版装饰器
        语法糖装饰器
        被装饰的函数有可变参数和关键字参数
        语法糖装饰器嵌套
        多个装饰器
            多个装饰器的装饰过程, 是离函数最近的装饰器先装饰, 然后外面的装饰器再装饰
            示例
                @deco1
                @deco2
                def func1(): xxx
            如上示例
                会先执行deco2,最后再执行deco1
        
        
        





拾肆.面向对象(014ObjectOriented)

    类创建遵循大驼峰命名法
    类中的方法至少有一个self参数,没有的话会报错,执行该方法时,回调用该方法的实例对象赋值给self
    类的构造函数是 __init__(self)方法, 初始化调用
    类的析构函数是 __del__(self)方法, 是对象在被垃圾回收时调用的, 它的执行意味着对象不能继续应用, 内存回收了
        示例
            p = Person()
            del p
        如果手动del, 那么__del__方法会立即执行
    
    封装和继承(encapsulation_inheritance)
        封装
            私有属性/方法(由双下划线开头)
                class Person:
                    name = 'anglee'
                    __age = 30
                实际上私有属性是将 __age 改为了 _Person__age (_类名__属性名), 了解即可, 非必要不要这样操作
                无法通过实例对象访问, 子类也不会继承私有属性, 不可以通过 from xxx import * 导入
                    p = Person()
                    p._Person__age
            隐藏属性/方法(由单下划线开头)
                可以通过实例对象访问, 子类会继承隐藏属性, 可以通过 from xxx import * 导入
                
        单继承
            pass 关键字是用来处理缩进而不报错用的, pass就是一个占位符
            多重继承
                A/B/C C继承B,B继承A,那么C就拥有A和B的所有属性和方法

        方法的重写
                在子类直接重写即可, 自己类有就会优先用自己类的
                子类主动重写父类方法(两种方法)
                    # Father.money(self)
                    # super(Son, self).money()
                    # 可以简写为 super().money()

        新式类
            如下三种写法在python3中都是等价的
                class Person:
                class Person():
                class Person(object):
            object是python中的顶级父类, 所有的类都继承自object类
            
        多继承
            当多个父类有相同的属性或方法时, 会用就近原则
                示例
                    class Son(Father, Mather):
                        pass
                    son = Son()
                    son.money()
                    son.appearance()
                如上, 爸爸妈妈都有money方法, son继承Father的, 如果想继承Mather的, 那就 class Son(Mather, Father) 将Mather提前
                可以通过 Son.__mro__查看同名属性方法的继承优先级
            

        多态
            多态的前提是继承和方法重写, 即调用同名方法时自动执行各自的实现, 使子类拥有不同的实现
            python3中类的静态方法要用 @staticmethod 修饰. 用类名和实例对象都可以调用静态方法
            

        
    单例模式和魔法方法(single_pattern_magic_method)
        实例构造器和初始化器(__new__和__init__)
            __new__方法可以在内存中为对象分配空间, 返回对象的引用
            __new__方法一定要 return super().__new__(cls), 否则示例的对象将会为None
            因为__new__就是给对象分配内存空间的, 如果不返回就不会分配所以实例对象会为None
            __new__是会在__init__之前执行, 当 __new__ 返回的不是该类实例时, __init__ 就不会被调用
            若 __new__ 返回该类实例, 则继续执行 __init__; 若返回其他对象或 None, 则不会调用 __init__
            __new__对象创建方法或实例构造器, __init__对象初始化方法或初始化器
            __new__的cls是类对象, super().__new__(cls)是实例对象
            
        单例模式
            单例模式的核心就是 类实例出来的多个对象必须是同一个.
                示例
                    s1 = Singleton()
                    print('s1: ', s1)
                    s2 = Singleton()
                    print('s2: ', s2)
                比如如上代码 s1 和 s2肯定不会是同一个对象, 但是通过重写__new__实现单例模式, 就可以让 s1 和 s2是同一个内存地址也就是完全的同一个对象
            通过重写__new__实现单例模式
                class Singleton(object):
                    obj = None
                    def __new__(cls, *args, **kwargs):
                        print('singleton 的 __new__')
                        if cls.obj == None:
                            cls.obj = super().__new__(cls)
                        return cls.obj
                    def __init__(self):
                        print('singleton 的 __init__')
            还可以通过模块导入实现单例模式
                因为模块就是天然的单例模式
                    from pyfile01 from test as test01
                    from pyfile01 from test as test02
                    print('test01: ', id(test01))
                    print('test02: ', id(test02))
                
        魔法方法
            即python内置的方法
            __str__/__call__/__doc__/__module__/__class__ 等等等....
            









拾伍.文件操作(015FileOperations)
    
    文件对象方法
        open(path/name,mode)         创建一个file对象,默认是只读模式打开
            mode
                | `"r"`  | 只读, 文件必须存在  |
                | `"w"`  | 写入, 不存在则创建  |
                | `"a"`  | 追加, 不存在则创建  |
                | `"x"`  | 创建, 存在则报错 |
                | `"r+"` | 读写, 文件必须存在  |
                | `"w+"` | 读写, 清空文件    |
                | `"a+"` | 读写, 追加      |
                | `"rb"`  | 二进制只读(bytes), 文件必须存在  |
                | `"wb"`  | 二进制写入(bytes), 不存在则创建  |
                | `"ab"`  | 二进制追加(bytes), 不存在则创建  |

        read(n)                 n表示从文件中读取的数据的长度,没有n时默认一次性读取文件的所有内容
        readline()              一次读取一行内容
        readlines()             按照行的方式一次读取全部内容
        write()                 将指定内容写入文件
        close()                 关闭文件
        
    with关键字
        with open(name)作用就是代码执行完, 系统会自动调用close函数, 省略关闭文件的步骤
            示例代码如下:
                with open('text1.txt','w') as file:
                    file.write('emmmmm......')
                    print('file.closed = ', file.closed)
                print('file.closed = ', file.closed)
        实际上 with 要求右边的对象必须是一个上下文管理器, 而使对象是一个上下文对象, 就必须声明有enter和exit这两个魔法方法.
            示例代码如下:
                class Person:
                    def __enter__(self):
                        print("进入上下文")
                        # 可返回任意对象, 通常返回自己
                        return self
                    def __exit__(self, exc_type, exc_val, exc_tb):
                        print("退出上下文")
                
                # 实例对象就是上下文管理器
                obj = Person()
                
                with obj as ctx:
                    print("在 with 块中操作 ctx")
            示例代码:
                class Person:
                    pass
                obj = Person()
                那么这个普通对象就不能用with了, 因为不是上下文对象
    
    目录操作
        os.rename(old,new)              目录重命名
        os.rmdir(dirname)               删除目录
        os.mkdir(dirname)               创建目录
        os.getcwd()                     获取当前目录
        os.listdir(dirname)             获取目录列表
        os.remove(filename)             删除文件


        






拾陆.迭代器和生成器(016IteratorAndGenerators)
    
    可迭代对象(Iterable)
        可以通过for.in这类语句遍历读取数据的对象
        str, list, tuple, dict, set
        条件
            实现__iter__()魔法方法
        isinstance()
            判断一个对象是否是可迭代对象, 或是一个已知的数据类型
    迭代器(Iterator)
        迭代器对象一定是可迭代对象, 可迭代对象可以通过 iter() 方法转换成迭代器对象
        如果一个对象拥有__next__()和__iter__()方法, 是迭代器对象
        如果一个对象只有__iter__()方法, 则它是一个可迭代对象
        凡是可以用for循环遍历的都是可迭代对象
        凡是可以用next()方法遍历的都是迭代器对象
        迭代器协议
            对象必须提供一个next方法, 执行该方法要么就返回迭代中的下一项, 要么就引发StopIteration异常
        自定义迭代器类
            两个特性
                __iter__() 和 __next__()
    生成器(Generator)
        Python中使用了 yield 的函数被成为生成器(generator)
        生成器的机制就是一边计算一边循环
        生成器有两种定义方式
            生成器表达式
                类似于列表推导式
                    列表推导式回顾
                        for i in range(5):
                            print(i*5)
                        列表推导可以这样写
                            li1 = [i*5 for i in range(5)]
                            print(li1)
            生成器函数
                def gen3(n):
                    li = []
                    for i in range(n):
                        yield i
                
                gen03 = gen3(5)
                print(next(gen03))
                print(next(gen03))
                print(next(gen03))
                print(next(gen03))
                print(gen03.__next__())
    可迭代对象/迭代器/生成器三者关系
        可迭代对象能被 for 遍历, 迭代器是能被逐个取值的对象, 而生成器是一种特殊的迭代器, 用 yield 动态生成数据.
        包含关系:
            所有生成器都是迭代器, 所有迭代器都是可迭代对象.







拾柒.线程进程和协程(017ProcessAndThreadAndCoroutine)

    多线程
        线程之间执行是无序的
        线程之间共享资源
        资源竞争
    
    












零、壹、贰、叁、肆、伍、陆、柒、捌、玖、拾;