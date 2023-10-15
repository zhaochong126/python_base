'''
作用域：函数内的参数在外部一般是不能访问的
全局作用域：在全局都有效，可以在程序任意位置被访问
函数作用域：在函数调用时创建，在函数结束时销毁
命名空间：
locals():获取当前作用域的命名空间

'''
# def f1():
#     a = 10
#
#     def f2():
#         print(a)
#     f2()
# f1()
# a=1
# def f1():
#     pass
# print(locals().items())#两个命名空间
#

a=1
def f1():
    global b
    b = 2
    print(locals())
f1()