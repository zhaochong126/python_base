'''
闭包的含义：在一些语言中，在函数中可以（嵌套）定义另一个函数时，如果内部的函数引用了外部的函数的变量，
          则可能产生闭包。闭包可以用来在一个函数与一组“私有”变量之间创建关联关系。在给定函数被多次调用的
          过程中，这些私有变量能够保持其持久性。
@staticmethod：将函数定义为静态方法
@classmethod：将函数定义为类方法
@property：将函数定义为属性方法
'''

# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print('前')
#         func(*args, **kwargs)
#         print('后')
#     return wrapper
#
# @my_decorator
# def say_hello(name):
#     print('hello', name)
# say_hello('zhaochong')




#计时器
# import time
# def timer(func):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         result = func(*args,**kwargs)
#         end_time = time.time()
#         print(f'{func.__name__} 执行时间：{end_time-start_time:.2f}s')
#         return result
#     return wrapper
# @timer
# def test_func(n):
#     num = 0
#     for i in range(n):
#         num+=i
#         print(num)
# test_func(10000)


