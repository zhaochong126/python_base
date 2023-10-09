#定义功能界面函数
def info_print():
    print('请选择功能------------')
    print('1,添加学员')
    print('2,删除学员')
    print('3,修改学员')
    print('4,查询学员')
    print('5,显示所有学员')
    print('6,退出系统')
    print('-'*20)
info = []
def member_add():
    dict1 = {}
    name = input('请输入姓名：')
    number = input('请输入电话： ')
    id = input('请输入学号： ')
    global info
    for i in info:#判断是否重名
        if name == i['姓名']:
            print('姓名重复，请重新输入。')
            return#退出当前函数，后面的代码不执行


    dict1['姓名'] = name
    dict1['手机号'] = number
    dict1['学号'] = id
    # print(dict1)
    info.append(dict1)
    print('添加成功')
    # with open('1.txt', mode='w', encoding='utf-8') as f:
    #     f.write(str(info))
    # print(info)
def member_del():
    name_del = input('请输入要删除的姓名')
    for i in info:
        if name_del == i['姓名']:
            info.remove(i)
            print('删除成功')
            break
    else:
        print('学员不存在')

    # print(info)

def member_change():
    name = input('请输入你要修改的姓名： ')
    for i in info:
        if name == i['姓名']:
            i['姓名'] = input('请修改姓名： ')
            i['学号'] = input('请修改学号： ')
            i['手机号'] = input('请修改手机号： ')
            for i in info:
                if name != i['姓名']:
                    info.append(i)
                    print('修改成功')
                    return
            else:
                print('重名了，请重新修改')
    else:
        print('姓名不存在')
# print(info)


def member_rearch():
    name = input('请输入你要查询的姓名： ')
    for i in info:
        if name == i['姓名']:
            print(i)
    else:
        print('查无此人')

def member_all():
    print(info)





while True:
    #显示功能界面
    info_print()

    #用户输入功能序号
    user_num = int(input('请输入功能序号：'))

    #按照不同序号，执行不同功能
    if user_num == 1:
        # print('添加')
        member_add()
    elif user_num == 2:
        # print('删除')
        member_del()

    elif user_num == 3:
        # print('修改')
        member_change()
    elif user_num == 4:
        # print('查询')
        member_rearch()
    elif user_num == 5:
        # print('所有学员')
        member_all()
    elif user_num == 6:
        # print('退出')
        break
    else:
        print('你输入了错误的数字')


