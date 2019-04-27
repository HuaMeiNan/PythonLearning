# -*- coding: utf-8 -*-
from functools import reduce


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print("测试成功")
else:
    print('测试失败')

print("-" * 50)


def normalize(name):
    b = name.capitalize()
    return b


L1 = ['adadm', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('-' * 50)


def str2float(s):
    def disy(s):
        dis = {'0': 0, '1': 1, "2": 2, '3': 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, '.':'.'}
        return dis[s]
    b = list(map(disy, s))
    if '.' in b:
        a = b.index('.')
        c = len(b) - a -1
        b.remove(".")
        d = reduce(lambda x, y: (x*10 + y), b)
        return d/10**c
    if '.' not in b:
        return reduce(lambda x, y : x * 10 + y, b)


print('str2float(\'123.456\')=', str2float('123.456'))
print('str2float(\'123.456\')=', str2float('12.3456'))
print('str2float(\'123.456\')=', str2float('123456'))

print('-' * 50)


def by_name(t):
    return t[0]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L3 = sorted(L, key=by_name)
print(L3)


def by_score(t):
    return t[1]


L4 = sorted(L, key=by_score,reverse=True )
print(L4)



R = list(filter(lambda x : x % 2 == 1, range(1,20)))
print(R)

print('-' * 50)
# 修饰函数  修饰器

import functools

def log(func):
    def wrapper(*args, **kw):
        print('call %s' %(func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("ww")

now()

def log2(text):
    def dict(func):
        def wrapper(*args, **kw):
            print("%s %s():" %(text, func.__name__))
            return func()
        return wrapper
    return dict

@log2('name')
def biu():
    print("xuan")

biu()



