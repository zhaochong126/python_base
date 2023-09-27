demo = [1, 2, 3, 4, 5]
# a, b, c, d, e = demo
# print(a) # 1 定长
# a, b, *c = demo
# print(a, b, c)  #1 2 [3, 4, 5],* 使得不定长
a = 1
b = 2
a, b = b, a
print(a, b)