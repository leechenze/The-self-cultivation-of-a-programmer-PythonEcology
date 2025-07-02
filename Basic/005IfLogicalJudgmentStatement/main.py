





score = int(input("请输入学生分数（0-100）："))

if 90 <= score <= 100:
    print("录取：清华大学或北京大学")
elif 80 <= score < 90:
    print("录取：西安交通大学或西北工业大学")
elif 60 <= score < 80:
    print("录取：长安大学")
elif 0 <= score < 60:
    print("录取：长治学院")
else:
    print("分数无效，请输入0到100之间的整数")



