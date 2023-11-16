'''
递归函数：需要有断点
闭包：如果在一个内部函数内，对在外作用域的变量进行引用，那么内部函数被认为时闭包，
闭包 = 内部函数 + 定义函数时的环境
装饰器：需要返回函数，不然会发生错误 TypeError: 'NoneType' object is not callable
'''
import time
# x=1
# def func():
#     global x
#     if x == 100:
#         print('递归结束')
#     else:
#         print(x)
#         x+=1
#         return func()
# func()


#闭包函数
# def f():
#     x = input()
#
#     def g():
#         start = time.time()
#         time.sleep(1)
#         print(x)
#         over = time.time()
#         print(over - start)
#     return g
# f()()

# def foo():
#     print('zhaochong')
#     time.sleep(1)

def show_time(func):
    def inner(*args):
        start = time.time()
        func(*args)
        over = time.time()
        print(f'运行了{over-start}秒')
    return inner

# show_time(foo)
sum = 0
# @show_time  #等价于foo=show_time(foo)
#
# def sum_1(*args):
#     global sum
#     for i in args:
#         sum += i
#     time.sleep(1)
#     print(sum)
#     # return sum
# # print(sum_1(1,31123,312,312,3,1))
# sum_1(1,123,12,3,1)