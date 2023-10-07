'''
继承
多级继承：mro()查看继承顺序
继承重构：直接在子类中定义一个与父类相同名称的函数
重后调用父类原函数：super()
如果一个子类继承了两个父类，想要继承的话先考虑第一个，第一个如果有多个父类，考虑第二个。
isinstance:判断对象是否属于指定类型。
方法重载：在一个类中，定义了多个同名，参数不同的函数，在调用方法时，根据传递的参数类型进行选择
多态性重构：根据不同类的继承实现不同的功能。
多态性——类型转换：将一个对象视为其父类或者接口类型进行使用，以适应不同的类型和需求。
'''


# class Father:
#     def __init__(self, name):
#         self.name = name
#
#     def run(self):
#         print(f'{self.name} is running...')
#
#
#
# class Son(Father):
#     def bark(self):
#         print(f'{self.name} is barking...')
#
#
# zhao = Son('zhao')
# Father.run(zhao)
# Son.bark(zhao)



# 多级继承:需要设计继承顺序

# class Fun1:
#     def fun1(self):
#         print('a')
#
# class Fun2(Fun1):
#     def fun2(self):
#         print('2')
#
#
# class Fun3(Fun2):
#     def fun3(self):
#         print('3')
#
#
# s = Fun3()
# s.fun3()
# print(Fun3.mro())#查看继承顺序


#
class Father:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f'{self.name} is running...')



class Son(Father):
    def bark(self):
        print(f'{self.name} is barking...')

    def run(self):
        super(Son, self).run()#可以继续使用父类的方法
        print('代码重构')


zhao = Son('zhao')
Father.run(zhao)
Son.bark(zhao)
zhao.run()


