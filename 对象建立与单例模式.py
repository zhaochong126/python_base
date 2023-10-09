'''
__new__():用于创建类的新实例。
先建立对象再初始化
单例模式：类实例 是 同一个对象（第一次实例是新建对象）
'''

class Demo:
    _instance = None
    def __init__(self, name):
        self.name = name
        print('init')


    def __new__(cls, *args, **kwargs):
        print('new')
        #super（）默认情况下， 寻找当前的父类
        if cls._instance is None:#是否时第一次实例化建立对象
            cls._instance = super().__new__(cls)
        # return super().__new__(cls)
        return cls._instance#如果不是第一次建立对象则返回同一个对象
demo1 = Demo('demo1')
demo2 = Demo('demo2')
demo3 = Demo('demo3')

# print(demo1.name)
# print(demo2.name)
print(demo1)
print(demo2)
print(demo3)