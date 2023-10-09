'''
字典：删除使用del


'''
# print([i for i in range(10)])#列表生成式
# print([i*i for i in range(10)])
# print([i*(i+1) for i in range(10)])
# print([i for i in range(10) if i%2==0])
# print([i+j for i in 'abc' for j in '123'])
name = 'zhao'
age = 10
height = 180.0
print('我是%s 我今年%d 我身高%2f' % (name, age, height))# 格式化输出
print('我叫{},今年{}岁，身高{}'.format(name, age,height))
print(f'我叫{name},今年{age}岁，身高{height}')
dict = {'zhoa':10, 'chong':11, 'cao':12}
print('zhao' in dict)
print('zhoa' in dict)
print(10 in dict.keys())#判断只能判断键
print(10 in dict.values())