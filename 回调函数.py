#回调函数是指一个函数作为参数传递给另一个函数，并在需要时被调用。
#常被用于异步编程，事件处理等场景中，可以让代码更加灵活和可维护。
# def demo(a):
#     return a * 10
# def print_demo(callback, int_data):
#     if int_data > 0:
#         return callback(int_data)
#     else:
#         return None
#
#
# data = print_demo(demo, 12)
# print(data)

def demo(a: float, b):
    return a+b
print(demo(1.0, 2))