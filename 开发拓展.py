'''
hasattr():判断对象是否有某个属性
getattr():获得对象某个属性值
setattr():给对象某个属性赋值
.同级目录
..上一级目录
绝对路径：避免转义在路径前加r，或者把'\'换成'/'
os模块：getcwd()返回当前目录的路径
chdir.(path)改变当前目录到指定路径，(path：要切换的新路径)
listdir():列出当前目录下的所有文件和子目录
mkdir(path)，makedir(path):分别用于创建一个新目录和递归地创建一个目录及其所有的子目录。
rmdir(),removedirs()
rename(str, dst)  src原始路径，dst目标路径。
remove(path):删除文件
os.path.exists(path):指定文件路径是否存在
os.path.join(path,path):合并两个路径
os.path.abspath(path):获得绝对路径
'''
import os

# class Demo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
# p = Demo('zhao', 18)
# print(hasattr(p, "name"))
# print(getattr(p, 'name'))
# setattr(p, 'name', 'zhaochong')
# print(p.name)

# current_dir = os.getcwd()#获取当前目录路径
# print(current_dir)
# print(os.listdir('F:\python入门课程代码'))
# os.makedirs('./zhao/chong/ni/hao')
# os.mkdir('./bu')
# print(os.path.exists('./特殊方法.py'))