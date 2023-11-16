'''
*args:不定长位置参数，保存到元组中
**kwargs:不定长关键字参数，保存到字典中
装包：把散开的数据聚合在元组或者字典中
解包：*tuple，string，list
'''


# def demo1(*args,**kwargs):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#     print(kwargs.values())
#     print(kwargs.keys())
#
# demo1(1,2,3,4,4,a=1,b=2)

# def f1(*args):
#     print(args)
# tup1 = (1,2,3,4,4)
# f1(*tup1)#解包


# def demo2(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
# t = (1,1,1,1312,12,31,23,12,)
# demo2(*t)#*t是将元组中所有元素依次拿出来作为参数传入



# def fn1():
#     print('waiceng')
#     def fn2():
#         print('neiceng')
#
#     return fn2()
# print(fn1())


# def f2():
#     return 0
# print(f2())
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

# def fn1(a, b):
#     print(a + b)
#
#
# fn1(1, 2)
#
#
# # 第二题
#
# def fn2(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
#
# fn2(1, 321, 3, 123)
#
#
# # 第三题
#
# def fn3(a):
#     if len(a) > 5:
#         print('长度大于五')
#     else:
#         print('长度小于五')
#
#
# fn3('helloworld')
#
#
# # 第四题
# def fn4(a, b):
#     print(a if a > b else b)
#
#
# fn4(1, 2)
#
#
# # 第五题
# def fn5(lst):
#     if len(lst) > 2:
#         return lst[0], lst[1]
#     else:
#         return lst
#
#
# list1 = [1, 2, 3, 4, 5]
# print(fn5(list1))



#1
def f1(a,b):
    return a-b
print(f1(1.2,2.1))
#2
def f2(n):
    if n%3==0 and n%5==0:
        print('Yes')
    else:
        print('No')

f2(15)
#3
def f3(a):
    list1=[]
    for i in a:
        if i < 0:
           list1.append(i)
    print(len(list1))
    print(list1)

f3([1,2,3,-1,-2,2])
#4
def f4(n):
    b = set(n)
    d = list(b)
    return d

print(f4([1, 2, 3, 4, 4, 5, 6, 2, 1]))