'''
__new__():用于创建类的新实例。
先建立对象再初始化
单例模式：类实例 是 同一个对象（第一次实例时新建对象）
'''

class Demo:
    _instance = None
    def __init__(self, name):
        self.name = name



    def __new__(cls, *args, **kwargs):
        #super（）默认情况下， 寻找当前的父类
        if cls._instance is None:#是否时第一次实例化建立对象

            return super().__new__(cls)
demo1 = Demo('demo1')
demo2 = Demo('demo2')

print(demo1.name)
print(demo2.name)