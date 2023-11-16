'''
字典：
clear():清空字典键值对
get():根据key获取value,不存在时打印None
update():更新字典
items():获取键值对到列表中
pop():获取指定value，删除这个键值对
setdefault():获得键对应的值，如果不存在则新建一个键值对


集合：无法存储字典，列表，集合这些数据类型，否则报错
创建新集合时使用set()而不是{}，否则默认为字典
set.add():添加对象
set.update():参数为序列类型，会将每一个元素迭代添加到序列中
set.pop():随机删除，但是pycharm默认删除第一个元素
set.discard():同remove，但是没有该元素也不会报错
set.clear():清空集合
del:删除集合

'''
# car ={'zhao':1, 'chong':2}
# print(car.get('zhao'))
# # print(car.get('zhoa'))
# list1 = car.items()
# list2 = car.keys()
# list3 = car.values()
#
# print(list1)
# # print(list(list1))
# print(list2)
# print(list3)
# print(car.pop('zhao'))
# print(car.setdefault('zhao', 2))
# print(car.setdefault('zhao', 1))#不会改变字典的值
# print(car.setdefault('bu', 1))

# car = {'zhao': 1, 'chong': 2}
# for i in car.items():  #('zhao', 1)  ('chong', 2)，放在元组中
#     print(i)

# set1 = {1,3,4,3,4,5,6,2,1,2}
# print(set1)#集合本身是无序的，{1, 2, 3, 4, 5, 6}
#
# set1.update('10')# {1, 2, 3, 4, 5, 6, '1', '0'}
# set1.update((13, 43, 10))# {1, 2, 3, 4, 5, 6, 10, 43, 13, '0', '1'}
#
# print(set1)
# set1.remove('1')
# set1.remove(1)
# print(set1)
# set1.discard('100')
# print(set1)
# set1.clear()
# print(set1)#set()


# ifno = {'zhoa':1,'zahhd':3,'dada':2}
# for i in ifno.keys():
#     print(i)
# tup_1 = (('dada',1),('daddaa',2),('daa',14))
#
# c=dict(tup_1)
# print(c)

# set1 = {1,31,23,12,31,2}
# set1.update(''a)
# print(set1)

#字典
my_dict={}
tup_1 = (('apple',3),('banana',6),('orange',4))
my_dict.update(tup_1)
print(my_dict)
print(my_dict.get('banana'))
a = my_dict.get('orange')
my_dict['orange'] = int(a)+2
print(my_dict)
my_dict.pop('apple')
print(my_dict)
print('grape' in my_dict)
a = my_dict.values()
values = []
for i in a:
    values.append(i)
print(values)


#集合
my_set = set()
list1 = ['apple','banana','orange']
for i in list1:
    my_set.add(i)
print(my_set)
my_set.remove('apple')
print(my_set)
my_set1 = {'kiwi','grape'}
print(my_set|my_set1)
print(my_set&my_set1)
print(my_set-my_set1)
# print(my_set in my_set1)
# 判断子集
print(my_set <= my_set1)
print(my_set.issubset(my_set1))