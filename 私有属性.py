class Demo():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


# demo_obj = Demo('nihao', 18)
#
# print(demo_obj._name)#nihao

    def get_name(self):
        return self.__name

l = Demo('nihao', 18)
print(l.get_name())
print(l._Demo__age)
print(vars(l))