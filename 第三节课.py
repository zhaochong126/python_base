'''
input接收的都是字符串类型
end默认是\n
除法后的结果是浮点数类型


'''
a = int(input())
b = int(input())
print(a+b)


name = input()
age = int(input())
print('%s:%d' % (name, age+10))


print('我叫赵冲', end=' ')
print(('年龄23'))

l = 'i kiss you'
a = l.split(' ')
print('主语是%s,谓语是%s,宾语是%s' % (a[0], a[1], a[2]))

username = input()
password = input()
print('账号是：%s 密码是：%s'%(username, password))