'''
iter:给可迭代对象变成迭代器对象
next:用来访问迭代器对象
迭代器函数有：map，filter，zip，reversed
'''
class MyIterator:
    def __init__(self,string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.string):
            raise StopIteration
        result = self.string[self.index]
        self.index += 1
        return result

myiter = MyIterator('hello world')
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
for i in myiter:
    print(i)