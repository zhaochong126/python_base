'''
pass : 保持结构完整
每个类默认继承了object（基本
类）


'''


class Person():
    name = 'nihao'
    def __init__(self, age):
        self.age = age


    @classmethod
    def demo(cls):
        print(cls.name)
        return cls.name + 'cao'


Person.demo()
# data = Person.demo()
# print(data)


# demo1 = Person(18)#传入参数
# demo2 = Person(28)
# demo1.name = '你好'
# Person.name = 'python'#类属性由类修改


# print(demo1.age)
# print(demo2.age)

