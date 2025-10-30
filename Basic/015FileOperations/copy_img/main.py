


### 复制图片小案例
# 读取二进制的图片文件
with open('./images/lovefly.png','rb') as file:
    imgBytes = file.read()
    print('img = ', imgBytes)
# 复制二进制的图片文件
with open('./images/loveflyCopy.png','wb') as file1:
    file1.write(imgBytes)

