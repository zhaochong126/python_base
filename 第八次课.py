'''
实参负责给形参赋值

'''
# def demo_1(a, b, c):
#     print(a*b*c)
#
# demo_1(1,2,3)
# def demo_2(name):
#     print(f'{name},欢迎你')
#
# demo_2('赵冲')
#
# def demo_3(a,b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
#
#
# demo_3(2,3)

# def login_in():
#     username = 'root'
#     pasword = 123456
#     user = input()
#     password = int(input())
#     if user == username and password == pasword:
#         print('登陆成功')
#     else:
#         print('登录失败')
# login_in()

#1
def f1(a,b,c):
    print(a+b+c)
f1(1,2,3)
#2
def f2(name):
    print(f'{name},欢迎你！')
f2('赵冲')
#3
def f3(a,b):
    print(a if a>b else b)
f3(1,2)
#4
def f4(list1):
    if len(list1) > 2:
        print(list1[0:2])
    else:
        print(list1)
f4([1,2,3])
#5
def f5(list2):
    sum = 0
    for i in list2:
        sum += int(i)
        print(sum)
f5([1,2,3])
#6
def f6(n):
    if len(n) == 0:
        print('该对象元素为空')
    else:
        print(n)
f6([])
#7
def f7(a):
    dict1={'R':'红色','G':'绿色','B':'蓝色','A':'透明色'}
    if a in dict1.keys():
        print(dict1[a])
    else:
        print('颜色不存在')
f7('R')