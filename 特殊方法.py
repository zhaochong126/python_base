# class Myclass:
#     def __call__(self, *args, **kwargs):
#         return args * 2, kwargs
#
# obj = Myclass()
# result = obj(1, 2, 3, a=1, b=2)
# print(result)

class Person:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return f'This person\'s name is {self.name}'

name = Person('zhaochong')
print(name)


