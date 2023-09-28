#闭包函数
# def demo_func():
#     name = '张三'
#     def geets():
#         return name + '内部函数'
#     return geets
#
#
#
#
# demo = demo_func()
# print(demo())


#内嵌函数
def outer():
    def inner():
        print('正在执行内部函数')

    inner()
outer()