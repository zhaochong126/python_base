# def add(a, b):
#     return a + b
# # print(add(num, 2))# a， b都是位置参数
# print(add(a=num, b=2))#a和b是关键字参数

#默认参数
# def add(a, b=2):#默认参数
#     result = a + b
#     print(f'The sum of {a} and {b} is {result}')
#
#
# add(num)
# add(num,3)
'''
不定长参数
不定长位置参数*
关键字不定长**

'''
# def add(*args):#封装成元组
#     print(type(args))
#     result = 0
#     for arg in args:
#         result += arg
#     return result
# print(add(num, 2, 3, 4))
# def greet(**kwargs):#不定长关键字参数
#     print(kwargs)# 字典：{'Alice': 'Hello', 'Bob': 'World'}
#     for name, message in kwargs.items():
#         print(f'{message}, {name}')
#

def greet(name, *args, age, **kwargs):
    # print(kwargs)
    print(name)
    print(*args)
    print(age)
    print(kwargs)
    # for name, message in kwargs.items():
    #     print(f'{message}, {name}')


greet('zhaochong', 1, 2, 3, 4, age=1, Alice='Hello',Bob='World')