'''
字符串方法：
str.find(str, beg=0, end=len(string))
    str:指定检索的字符串
    beg:开始的索引
    end:结束的索引，默认为字符串的长度
        find找不到返回-num
        index找不到报错
count():寻找字符出现的次数
strip():去除字符串两边的空格，换行符，制表符
startswith():以什么开始，返回值为布尔值
endswith():以什么结束
isdigit():是否为全数字
isalpha():是否为全字母
lower(),upper():字符串大小写
split():字符串切割
replace():替换
join():将字符串转换成列表时使用
len()：求长度
切片：s[::] 前标：后标：步长
六大标准类型：整型，字符串，元组，列表，集合，字典

'''
# s = 'Hello World'
# print(s.find('H'))#num
# print(s.find('World'))#6
# print(s.find('o', num))#4

# s = input()
# print(s.lower())#SJJIjsjjsa,sjjijsjjsa

# s = 'my name is zhaochong'
# print(s.split(' '))


# arr = ['hello', 'ni', 'hao']
# print(' '.join(arr))#hello ni hao

# l = 'h e l l o w o r l d'
# a = l.split(' ')
# print(a)
list1 = ['h', 'e', 'l', 'l', 'o', ',', 'w', 'o', 'r', 'l', 'd']

print(''.join(list1))

list2 = ['abs', '左手', '种植通左手', '湖南人']
for i in list2:
    if len(i)>3:
        print(i)
    else:
        continue

list3 = ['a', 'e', 'i', 'o', 'u']
list4 = []
str = input()
for i in str:
    if i in list3:
        list4.append(i)
    else:
        continue
print('a:', list4.count('a'))
print('e:', list4.count('e'))
print('i:', list4.count('i'))
print('o:', list4.count('o'))
print('u:', list4.count('u'))