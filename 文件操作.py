'''
文件打开：open(文件，'rwa')
文件：相对路径，绝对路径
模式：读r，写w，追加a
b---二进制模式
+—--读写模式
rb读取二进制数据
wb写入二进制数据
ab追加二进制
r+,w+:读打开，写打开，读写操作。
f.flush():保存数据
'''

# file_obj = open('demo.txt', 'r', encoding='utf-8')
# print(file_obj.read())#读取数据
# print(file_obj)#迭代器
# print(file_obj.readlines())#读取多行数据
# file_obj = open('demo.txt', 'w', encoding='utf-8')
# file_obj.write('nihao')
# file_obj = open('demo.txt', 'a', encoding='utf-8')
# file_obj.write('\nnihoa')
# file_obj.write('\nhello world')


# open('上下文管理器.py', 'a')
# with open('暂用.py', 'w') as f:
#     f.write('print("hello")')
# with open('暂用.py', 'r') as f:
#     data_user = f.read()
#     print(data_user)