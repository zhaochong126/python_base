# class Myclass:
#     def __call__(self, *args, **kwargs):
#         return args * 2, kwargs
#
# obj = Myclass()
# result = obj(num, 2, 3, a=num, b=2)
# print(result)

class Person:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return f'This person\'s name is {self.name}'

name = Person('zhaochong')
print(name)


