'''

break和continue：
break退出整个循环，
continue：退出本次循环
'''



# list1 = input()
# if list1 == "yes":
#     print('ok')
# else:
#     print(list1)
# print('hello world'*2)

# a = 0
# num = 0
# while a < 10:
#     a += num
#     num += a
#     # print(num)
#     print(a)
# sum = 0
# for i in range(0, 101):
#     sum += i
# print(sum)
#密码验证程序
# username = 'abc'
# password = '123456'
# max = 5
# for i in range(max):
#     u = input('请输入账号：')
#     p = input('请输入密码：')
#     if u == username and p == password:
#         print('成功登录')
#         break
#     elif i == 4:
#         print('你的账号已被冻结')
#         break
#     else:
#         print('密码错误，请重新输入：')


# 检查是否是闰年：
# year = int(input('请输入年份：'))
# if year % 4 == 0 and year % 100 != 0:
#     print('这个年份是闰年')
# elif year % 400 == 0:
#     print('这个年份是闰年')
# else:
#     print('这个年份不是闰年')


#计算1到100的和：
# a = 0
# sum = 0
# while a < 101:
#     sum += a
#     a += 1
# print(sum)

#九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{i}*{j}={i*j}\t', end='')
    print()

# a = int(input())
# b = int(input())
# if a>b:
#     print(a)
# else:
#     print(b)
# print(a if a>b else b)

# str1 = input()
# print(str1 if str1 == 'True' else 0)


# for i in range(0,101,2):
#     print(i)
# for i in range(1,6):
#     for j in range(1,10):
#         print('房间数为：', f'%d0%d' % (i,j))