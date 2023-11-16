'''
魔法方法：符合触发条件时，自动触发执行
析构方法通常被用来执行清理任务，例如释放资源，关闭文件等操作。

__del__:对象或者实例被销毁时自动调用
'''
class File:
    def __init__(self, path):
        self.path = path
        self.file = open(path, mode='r')
    def read(self):
        return self.file.read()
    def __del__(self):
        self.file.close()
        print('File %s closed.' % self.path)

file = File('test.txt')
print(file.read())
# print(dir(File))