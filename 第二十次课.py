'''
继承:
多继承:如果父类有相同属性，则继承第一个
'''
class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area



class Home():
    def __init__(self,area):
        self.area = area
        self.residue_area = area
        self.furniture = []


    def add_furniture(self, item):
        if item.area<self.residue_area:
            self.furniture.append(item.name)
            self.residue_area-=item.area
        else:
            print('剩余面积不够了')

    def __str__(self):
        return f'房子面积为{self.area},剩余面积为{self.residue_area},搬进的家具有{self.furniture}'

bed = Furniture('床',10)
home1 = Home(200)

home1.add_furniture(bed)
print(home1)





