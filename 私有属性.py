'''
私有属性只能在类内部被访问和修改，无法从外部直接访问和修改，从而保证了对象的封装性和安全性，
但是可以使用getter和setter进行访问和修改
单下划线是内部属性，可以外部访问
dir():查询对象中所有属性
vars()：返回一个字典，包含person对象所有实例变量和其对应的值

'''


class Demo():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_attribute(self):
        return self.__name

demo1 = Demo('zhao', 18)

print(demo1.get_attribute())#定义一个函数来获得私有属性


# class Demo():
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#
# demo_obj = Demo('nihao', 18)
# print(dir(demo_obj))
# print(demo_obj._Demo__age)#私有属性
# demo_obj._Demo__age = 10#修改私有属性
# print(demo_obj._Demo__age)
# print(vars(demo_obj))


#['_Demo__age', '_Demo__name', '__class__', '__delattr__', '__dict__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']






