# -*- coding: utf-8 -*-
# 函数式编程


# Python允许在定义一个函数时，将一个函数作为参数，这样定义的函数被称为高阶函数。


# map
# 接收一个函数f和一个迭代器i，将f作用到每一个元素上，搜集起来，返回一个新的迭代器。

# 练习1：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    first = [name[0].upper()]
    rest = [x.lower() for x in name[1:]]
    return str.join("", first + rest)


# 测试:
names = ['adam', 'LISA', 'barT']
print(list(map(normalize, names)))
# Out:['Adam', 'Lisa', 'Bart']


# reduce
# 把一个函数作用在一个序列上
# 把结果继续和序列的下一个元素做累积计算
# 练习2：编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce


def prod(mults):
    return reduce(lambda x, y: x * y, mults)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# Out: 945


# 练习3 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    n = s.index('.')
    return reduce(lambda x, y: x * 10 + y, map(char2num, s[:n] + s[n + 1:])) / (10 ** n)


print('str2float(\'123.456\') =', str2float('123.456'))


# filter
# 根据传入的值决定是否丢弃函数。
# 练习4：利用filter()滤掉非回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(list(filter(is_palindrome, range(1, 1000))))


# Out: [1, 2, 3, ..., 949, 959, 969, 979, 989, 999]


# 装饰器 decorator
# 在函数运行前后做追加行为
# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)
# 如果是@log('execute')，则相当于now = log('execute')(now)


# 练习5：编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def log(func):
    def wrapper(*args, **kw):
        print("begin call %s" % func.__name__)
        result = func(*args, **kw)
        print("end call %s" % func.__name__)
        return result

    return wrapper


@log
def f():
    print("calling self")
    return "f result"


print(f())
