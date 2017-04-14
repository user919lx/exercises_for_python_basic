# -*- coding: utf-8 -*-
# Python 特别的函数构造方法


# 默认参数
def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l
for x in range(0, 3):
    if x < 1:
        print(add_end([x]))
    else:
        print(add_end())
# Out
# [0,'END']
# ['END']
# ['END']


# 用*表示个数可变的参数，会自动组装成一个tuple
def product(*numbers):
    s = 1
    for n in numbers:
        s = s * n
    return s


print(product(1, 2, 3, 4))
# Out
# 24


# 用*将list或tuple转为可变参数
print(*[1, 2, 3, 4, 5])
# 1 2 3 4 5


# 用**表示关键字参数，会自动组装成一个dict
def person1(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person1('Bob', 35, city='Beijing', location='Haidian')
# Out
# name: Bob age: 35 other: {'city': 'Beijing', 'location': 'Haidian'}


# 命名关键字参数,*号后面为关键字命名
def person2(name, age, *, city, job):
    print(name, age, city, job)
person2('Jack', 24, city='Beijing', job='Engineer')
# Out
# Jack 24 Beijing Engineer


# 汉诺塔问题
def move(n, a, b, c):
    # n==1时，直接从a 移动到 c
    if n == 1:
        print("%s --> %s" % (a, c))
    # n > 1 时，
    # 先将前 n - 1 个圆盘从a 经c 移至b
    # 再将最后的圆盘直接从a 移至c
    # 最后将剩下n - 1 个圆盘从b 经a 移至 c
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
move(3, 'A', 'B', 'C')
# Out:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
