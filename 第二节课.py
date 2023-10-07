'''
代码注意注释
['False', 'None', 'True', 'and', 'as', 'assert', 'async',
'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
科学计数法：120000 = num.2e5




'''
# import keyword   #键盘内部关键字
# print(keyword.kwlist)
# print(num.2e-3)

name = '赵冲'
age = 23
height = 183
hometown = '河南'
interest = 'Basketball'
base = 'True'
print('%s\n%s\n%s\n%s\n%s\n%s' % (name, age, height, hometown, interest, base))
print(name+'\n'+str(age)+'\n'+str(height)+'\n'+hometown+'\n'+interest+'\n'+base)


s = '人生苦短， 我学python'
print(s[2], s[4], s[6], s[-2])