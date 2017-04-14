# -*- coding: utf-8 -*-
# Python高级特性


# 列表生成式
# 简化生成列表的代码
# 可以使用 if 来筛选元素
l1 = ['Hello', 'World', 18, 'Apple', None]
l2 = [x.lower() for x in l1 if isinstance(x, str)]
print(l2)
# Out:
# ['hello', 'world', 'apple']


# 生成器
# 一边循环一边计算


# tuple生成器：
g = (x * x for x in range(10))
print(g)
# Out
# <generator object <genexpr> at 0x000000AAB5E69620>


# 函数生成器：使用yield来返回本轮循环生成的值
# 练习：杨辉三角生成器
def triangles():
    l = [1]
    while True:
        yield l
        l = [x+y for x, y in zip([0, *l.copy()], [*l.copy(), 0])]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
# Out:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]