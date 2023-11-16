'''
生成器(generator)
不会给你开辟内存空间
yield：可以暂停程序的执行并返回中间值，暂停函数运行
return:在函数中返回某个值，函数结束
send:发送值
fibonacii数列：f(n) = f(n-1) + f(n-2)
'''
def fibonacii():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

fib = fibonacii()
# print(next(fib))
for i in range(10):
    print(next(fib))