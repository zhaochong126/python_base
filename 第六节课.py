'''
字典：删除使用del
列表：
append():在列表末位添加元素
extend():添加列表到末位
insert():在指定位置添加元素
remove():默认删除第一个元素，根据值来删除
pop():根据索引删除值
del list:删除列表
del list[0]:根据索引值删除
clear():清空列表
改和查：根据索引来


'''
# print([i for i in range(10)])#列表生成式
# print([i*i for i in range(10)])
# print([i*(i+1) for i in range(10)])
# print([i for i in range(10) if i%2==0])
# print([i+j for i in 'abc' for j in '123'])
# name = 'zhao'
# age = 10
# height = 180.0
# print('我是%s 我今年%d 我身高%2f' % (name, age, height))# 格式化输出
# print('我叫{},今年{}岁，身高{}'.format(name, age,height))
# print(f'我叫{name},今年{age}岁，身高{height}')
# dict = {'zhoa':10, 'chong':11, 'cao':12}
# print('zhao' in dict)
# print('zhoa' in dict)
# print(10 in dict.keys())#判断只能判断键
# print(10 in dict.values())

#给定字符串拼接符拼接
str_1 = 'Hello'
str_2 = 'World'
print(str_1+str_2)
#使用占位符将一个名字和年龄拼接成一句话
name = '小明'
age = 18
print('我叫%s，我今年%d岁'%(name,age))
#使用join方法进行连接
word = ['I','love','python']
print('-'.join(word))
#使用format按照指定顺序连接
str_1 = '他'
str_2 = '真帅'
str_3 = '是吗？'
print('{}{}{}'.format(str_1,str_2,str_3))
#使用format按照下标连接
str_1 = '他'
str_2 = '真帅'
str_3 = '是吗？'
print('{0}{1}{2}'.format(str_1,str_2,str_3))
#使用format给变量重新命名进行字符串连接
print('{l1}{l2}{l3}'.format(l1='他',l2='真帅',l3='是吗'))

#使用f-format直接连接
str_1 = '他'
str_2 = '真帅'
str_3 = '是吗？'
print(f'{str_1}{str_2}{str_3}')
#将一个字符串转为大写
data_string = 'hello world'
print(data_string.upper())
#假设有一个字符串 "Hello, my name is John. I am 25 years old."，请完成以下操作(years old--岁的意思)
str_1 = 'Hello, my name is John. I am 25 years old.'
#1使用索引和切片获取并输出该字符串中的姓名（John）
print(str_1.index('John'))#18
print(str_1[18:22])
#2使用整数计算获取并输出该字符串中年龄的两倍
print(str_1.index('25'))#29
print(int(str_1[29:31])*2)
#3将该字符串中的名字（John）替换为另一个名字，并输出替换后的字符串
str_2 = str_1.replace('John','Kobe')
print(str_2)
#4使用字符串的格式化方法，将该字符串中的年龄替换为当前年份（2023）减去出生年份（出生年份为1980），并输出替换后的字符串。
birth_year = 1980
current_year = 2023
print(f'Hello, my name is John. I am {current_year-birth_year} years old.')