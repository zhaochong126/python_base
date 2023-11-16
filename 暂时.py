import time
from 第十二次课 import show_time

# sum=0
# @show_time
#
# def sum_1(*args):
#     global sum
#     for i in args:
#         sum += i
#     time.sleep(1)
#     print(sum)
# sum_1(1,123,12,3,1)






# list1 = list(input().split(' '))
# list2 = reversed(list1)
# print(' '.join(list2))

# l = input().split(' ')
#
# # print('Hello', l[0], 'and', l[num], '!')
# # print('Hello,%s and %s!' % (str(l[0]), str(l[num])))
# l1 = int(input())
# l2 = int(input())
# print((str(l1)+'大于等于'+str(l2)) if l1 >=l2 else (str(l1)+'小于'+str(l2)))
# print('123',end='\ddd')
# print('aaa',end='\t')
#
# a = 1
# b = 1
# # print(a == b)
# # print(a is b)
# print(id(a))
# print(id(b))

# dict1 = {'nihao':1,'nibuhao':2}
# print(str(dict1))

# def show_time(func):
#     start = time.time()
#     func()
#     over = time.time()
#     print(f'运行了{over-start}秒')
#     return func
#
# # show_time(foo)
# sum = 0
# @show_time
#
# def sum_1(*args):
#     global sum
#     for i in args:
#         sum += i
#     time.sleep(1)
#     print(sum)
#     return sum
# # print(sum_1(1,31123,312,312,3,1))
# sum_1(1,123,12,3,1)
# def show_time(func):
#     start = time.time()
#     func(*args)
#     over = time.time()
#     print(f'运行了{over-start}秒')
#     return func
# sum = 0
# @show_time

import random
# password = input('请输出你的密码：')
#
# if len(password) == 11:
#     if int(password[0]) == 1 and int(password[1]) in [3,4,5,8]:
#
#         player = input('请输入剪刀 石头 布：')
#         computer = random.choice(['剪刀','石头','布'])
#         print('computer输入的是',computer)
#         if (player == '剪刀' and computer == '布') or (player =='石头' and  computer == '剪刀') or( player =='布'and computer =='石头'):
#             print('player is the winner')
#         elif (computer == '剪刀' and player == '布' ) or (computer=='石头' and  player == '剪刀') or (computer =='布'and player =='石头'):
#             print('computer is the winner')
#         elif (computer == '剪刀' and player == '剪刀' ) or (computer=='石头' and  player == '石头') or (computer =='布'and player =='布'):
#             print('平局')
#         else:
#             print('please input 剪刀or 石头 or布')
#     else:
#         print('密码不正确')
# else:
#     print('密码没有十一位')


# class Nihao:
#     def __init__(self,name):
#         self.name = name
#
# nihao = Nihao('zhao')
# print(nihao.name)
# print(dir(nihao))

# list= [1,2,3]
# for i in list:
#     print(f'{i}', end=' ')

class F1():
    def __init__(self,name,age):
        print('1')

class F2():
    def __init__(self,name,age,height):
        print(2)

class F3(F1,F2):
    pass

F3('zhao',18)



