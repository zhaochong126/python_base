# demo = [i for i in range(10) if i%2 == 0]
# print(demo)#列表推导式
#
# key_1 = ['比赛', '友谊']
# value_2 = [num, 2]
# data = {key_1[i]:value_2[i] for i in range(len(key_1))}
# print(data)
key_1 = ['zhao', 'chong', 'ni', 'hao']#字典推导式
value_1 = [1, 2, 3, 4, 5]
num = len(key_1) - len(value_1)
if num > 0:
    data = {key_1[i]: value_1[i] for i in range(len(key_1) - num)}
    print(data)
    [data.setdefault(key_1[i], 10) for i in range(len(key_1) - num, len(key_1))]#将没有值的键赋值
    print(data)
else:
    data = {key_1[i]: value_1[i] for i in range(len(key_1))}
    print(data)