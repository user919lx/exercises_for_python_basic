# -*- coding: utf-8 -*-
# 一些需要特别注意的Python基础语法


# 1. 多行字符串 用三个引号表示
s1 = """line1
line2
line3"""
print(s1)
# Out:
# line1
# line2
# line3

# 2. 字符串前加r，不转义输出
s2 = "a\'b\'"
print(s2)
# Out:
# a'b'
s3 = r"a\'b\'"
print(s3)
# Out
# a\'b\'

# 3. 字符串格式化
# %d	整数
# %f	浮点数
# %s	字符串

s4 = 'Hello, %s, %.3f, %d' % ('world', 1.01, 4)
print(s4)
# Out:
# Hello, world, 1.010, 4

