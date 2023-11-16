'''
re.findall(pattern,string,flags):正则表达式
pattern:要匹配的正则表达式
string:在其中匹配的字符串
flags:参数可以指定正则表达式的匹配模式，如是否忽略大小写等
re.match(pattern,string,flags=0):字符串开头匹配字符表达式，返回的是match对象
group():查看匹配字符
span:查看匹配数据的索引值区间
re.search:在字符串中搜索与正则表达式匹配的子串，并返回一个Match对象,只返回第一个match对象
.是匹配任意字符
^是匹配字符串开头
$是匹配字符串结尾
(?P<变量名>)给提取到的数字命名

'''
import re
#定义正则表达式 '\d+',它可以匹配一个或多个数字字符
# \d 数字0-9
# +  匹配一个或多个字符
# \s* 匹配多个或者零个空格字符
# \w 匹配任意字母，数字，下划线
# pattern = r'\d+'
# string1 = '131231The price of the apple is 2 dollars, and the price of the orange is 1 dollar.'
# # result = re.findall(pattern,string1)
# # print(result)
# match_result = re.match(pattern,string1)
# print(match_result)
# print(match_result.group())
# print(match_result.span())



# string1 = '我的电话是14790185224，请给我打电话'
# pattern = r'1[3456789]\d{9}'#第一位是1，第二位是3到9中的一个，后面九位进行匹配
# result = re.findall(pattern,string1)
# print(result)

# string = '<p>我是一段文本</p>'
# pattern = r'<.*?>'
# replacement = ''
# result = re.sub(pattern,replacement,string)
# print(result)

ret = re.sub(r"php","python","I love php")#替换

