'''
实参负责给形参赋值

'''
def demo_1(a, b, c):
    print(a*b*c)

demo_1(1,2,3)
def demo_2(name):
    print(f'{name},欢迎你')

demo_2('赵冲')

def demo_3(a,b):
    if a > b:
        print(a)
    else:
        print(b)


demo_3(2,3)