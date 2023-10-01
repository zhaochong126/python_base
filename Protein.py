class Protein:
    def D1(self):
        print("AGHFQERLGAARAGAFDV" in "VQLVQSGAEVKKPGSSVKVSCEASGGTFSKYAFSWVRQAPGQGLEWMGGIIPIFHTTNYAOKFOGRVTISADEFNSRAYMELTSLRSEDTAVYYCARGAGSTPYNYYGMDIWGOGTTVTVSS")


    def D2(self):
        protein_1 = ['A', 'S', 'T', 'R', 'R', 'L', 'V', 'A', 'S', 'G', 'P', 'E', 'W', 'F', 'F', 'C', 'V', 'M']
        protein_2 = ['A', 'S', 'T', 'T', 'S', 'S', 'V', 'A', 'S', 'G', 'P', 'E', 'W', 'F', 'F', 'C', 'V', 'M']
        same_amino = [c for c in protein_1 if c in protein_2]
        print((len(same_amino)))

    def D3(self):
        protein_2 = ['A', 'S', 'T', 'T', 'S', 'S', 'V', 'A', 'S', 'G', 'P', 'E', 'W', 'F', 'F', 'C', 'V', 'M']
        # 创建一个空字典a，使用for循环在序列protein_1找到相同氨基酸
        a = {}
        for i in protein_2:
            # 使用count函数对氨基酸记数
            a[i] = protein_2.count(i)
        # 输出字典a，其key为氨基酸，对应value为其数量
        print(a)
        b = sorted(zip(a.values(), a.keys()), reverse=True)
        print(b)

    def D4(self):
        dict = {
            "A": "T",
            "T": "A",
            "G": "C",
            "C": "G",
        }
        a_input = reversed(input('输入的蛋白质序列是：'))

        list1 = list(a_input)
        # 用字典里的值代替列表list1中的值
        list1 = [dict[i] for i in list1]
        c = ''.join(list1)
        print(c)
        return c




    def D5(self):
        for i in range(1, 10):
            # 内循环控制乘数，范围从1到i，以确保只生成下半部分的乘法口诀表
            for j in range(1, i + 1):
                print(f"{j} * {i} = {i * j}", end='\t')  # 使用end='\t'来在同一行输出，并使用制表符分隔每个结果
            # 内循环结束后，换行以开始新的行
            print()

x = Protein()
x.D1()
x.D2()
x.D3()
x.D4()
x.D5()
