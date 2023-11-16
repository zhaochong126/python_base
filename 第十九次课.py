'''
类中函数相互调用要加 self，如上述代码中的c = self.add()+self.square()
pow(a, b):求a的b次方

__str__:写在类里，必须有返回值，返回类方法。
'''


class Person(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, z=16):  # 设置 默认变量 z =16,这只是个普通的局部变量，非实例变量，实例变量需要 self.z = z,这样定义
        sum = self.x + self.y + z
        return sum

    def square(self):
        squr = pow(self.x, 2) + pow(self.y, 2)
        return squr

    def add_square(self, z):  # 调用时传入变量，这也是个普通的局部变量，非实例变量
        c = self.add() + self.square() + z
        return c


student = Person(3, 4)
print(student.add())
print(student.square())
print('--------- 我是可爱的分割线-----------')
print(student.add_square(16))