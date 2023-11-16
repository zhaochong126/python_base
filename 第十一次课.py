'''
匿名函数：lambda 参数列表：运算表达式
abs():绝对值函数
sum():加法函数
round():四舍五入，有精度问题
map(func,seq):操作序列里的所有元素，返回一个迭代器，转列表后可以得到最终的值
reduce(func,seq):累加器，需要导包，只返回一个值，数值不能迭代，但是对象可以迭代
filter():过滤器
sorted(iter,cmp=None,key=None,reverse=False):
iter:可迭代对象
cmp:比较的函数
key:比较的元素

'''

# f = lambda x: x * x
# print(f(5))

# print(round(4.5))#在取4.5时失去精度

# def abs_sum(a,b,f):
#     return f(a)+f(b)
# res = abs_sum(-1,-2,abs)
# print(res)

# def new(n):
#     return -n
# def abs_sum(a,b,f):
#     return f(a)+f(b)
#
# res = abs_sum(-1,3,new)
# print(res)
# lst = [1,1,2,3,4,4]
# print(list(map(abs,lst)))

# reduce()
# from functools import reduce
# def sum(a,b):
#     return a+b
# lst = [1,1,2,3,4,4]
# res = reduce(sum,lst)
# print(res)
# from functools import reduce
# lst = [1,1,2,3,4,4]
# print(reduce(lambda x, y: x+y, lst))

# list1 = ['nihao:12','ahoh:44','dada:33']
# def f(x):
#     arr = x.split(':')
#     return int(arr[1])
#
# print(sorted(list1,key=f))
# print(sorted(list1,cmp=lambda x,y:cmp(x[1],y[1])))#?


# #1
# l1 = [-1,3,-5,-4]
# # l2 = []
# # for i in l1:
# #     l2.append(abs(i))
# # print(l2)
# print(list(map(abs,l1)))
#
# #2
# l3=['zhao','chong']
# def f1(x):
#     return x+'_xc'
# print(list(map(f1,l3)))
#
#
# #3
# str1 = '1 3 5 7 8'
# def int_new(x):
#     y = x.split(' ')
#     return y
# print(int_new(str1))
#
# str1 = '1 3 5 7 8'
# print(str1.split(' '))

def f():
    x=1
    def g():
        print(x)
    return g
f()()