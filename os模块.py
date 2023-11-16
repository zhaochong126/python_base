import os

# print(os.getcwd())#获取当前所处的目录位置

# os.chdir('os')#改变当前目录到指定目录
# print(os.getcwd())

# print(os.listdir())#返回目录的名字，以列表展示，path是路径

# os.mkdir('os1')#创建新的目录,单级目录创建

# os.makedirs(r'os/os1')#多级目录创建

# print(os.name)

# print(os.path.exists('os模块.py'))#判断文件是否存在

# now_dir = os.getcwd()
# data = os.path.join(now_dir,'./os')#路径拼接，有/时直接抛弃前面的参数./是从上一级目录开始拼接
# print(data)

# print(os.path.abspath('os模块.py'))#获取绝对路径
