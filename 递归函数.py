#递归函数：需要有多个判定结束的条件，来限制函数的调用。反复调用自身的函数。


def fact(x):
    if x == 1:
        return 1
    return x * fact(x-1)

print(fact(6))