'''
*args:不定长位置参数，保存到元组中
**kwargs:不定长关键字参数，保存到字典中
装包：把散开的数据聚合在元组或者字典中
解包：
'''


# def demo1(*args,**kwargs):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#     print(kwargs.values())
#
# demo1(1,2,3,4,4,a=1,b=2)

# def demo2(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
# t = (1,1,1,1312,12,31,23,12,)
# demo2(*t)#*t是将元组中所有元素依次拿出来作为参数传入

# def fn():
#     def fn2():
#         print('你好')
#     return fn2
#
# a = fn()
# print(a)
# a()
# print(b)
# print(1)
# print(print(print()))
# print(1)


# 第一题

def fn1(a, b):
    print(a + b)


fn1(1, 2)


# 第二题

def fn2(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


fn2(1, 321, 3, 123, )


# 第三题

def fn3(a):
    if len(a) > 5:
        print('长度大于五')
    else:
        print('长度小于五')


fn3('helloworld')


# 第四题
def fn4(a, b):
    print(a if a > b else b)


fn4(1, 2)


# 第五题
def fn5(lst):
    if len(lst) > 2:
        return lst[0], lst[1]
    else:
        return lst


list1 = [1, 2, 3, 4, 5]
print(fn5(list1))
