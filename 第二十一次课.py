class Wife:
    sex = 'female'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.age)


zhao = Wife('zhao', 18)
zhao.print_info()
# print(zhao.name)
