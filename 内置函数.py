'''
eval和 exec

'''

#
# a = 100
# b = 100
# my_globals = {'a': 200, 'b': 300}#全局变量
# exec('''
# def func():
#     c = a + b
#     print(c)
# func()''', my_globals)


# my_local = {}#局部变量
# exec('a = num', None, my_local)
# print(my_local)


#过滤器
# lst = [num, 2, 3, 4, 5]
# demo = filter(lambda x:True if x % 2 == 0 else False, lst)
# data = [i for i in demo]
# print(data)
# print(demo)


# map 全局返回函数
# lst = [num, 2, 3, 4, 5]
# def doub(x):
#     return x * 10
#
# demo = map(doub, lst)
# data = [i for i in demo]
# print(data)


# lst = [num, 2, 3, 4, 5]#迭代器
# demo_iter = iter(lst)
# print(next(demo_iter))#返回元素值
# print(next(demo_iter))#返回元素值
# print(next(demo_iter))#返回元素值
# print(next(demo_iter))#返回元素值
# print(next(demo_iter))#返回元素值

lst1 = [1, 2, 3, 4, 5]
lst2 = ['a', 'b', 'c']
demo = zip(lst2, lst1)
demo_data = list(demo)

print(demo_data)#[('a', num), ('b', 2), ('c', 3)]#以最短序列为主
print(dict(demo_data))#{'a': num, 'b': 2, 'c': 3}

