# =================conding: utf-8
"""
================================================================================

Author : Administrator
Created  on : 2021/2/24

E-mail: zh13997821732@163.com


================================================================================

"""
import numpy

# print('欢迎使用憨憨牌体重计算器')


# weight = float(input("请输入您的体重(kg):"))
# height = float(input("请输入您的身高（m）:"))
# BMI = round(weight / (height ** 2), 1)
# if BMI <= 18.4:
#     print("您的体重偏瘦，请多吃点~")
# elif 18.4 <= BMI <= 23.9:
#     print("您的体重正常，请继续保持！")
# elif 24.0 <= BMI <= 27.9:
#     print("您的体型[肥胖]，请少吃饭")
# elif BMI >= 28.0:
#     print("您的体重超标,建议您绝食")
# else:
#     print("您的输入有误，请重新输入！！！")

# name = str(input("请输入您的名字："))

# def method(a, b=[]):
#     b.append(a)
#     return b
#
#
# print(method(1))
# print(method(2))
# print(method(3))
# list_b = (5, 10)
# list(range(*list_b))
# a = lambda x, y, z: (y + z) * x
# print(a(5, 10, 15))

# lista=[]
# lista.append()
# for i in range(1, 4):
#     if i != 1:
#         print(i ** 2)
# lista = [i ** 2 for i in range(1, 4) if i != 1]
# print(lista)
# print(lista)
# c=5
# a = {}
# b = a.fromkeys((1, 2, 3, c), "a")
# print(b)
# import numpy as np
# a = np.arange(15).reshape(3, 5)
# print(a)


dic1 = {'name': 'tom', 'age': '18'}
print('my name is {name},age is {age}'.format(**dic1))
name = 'lili'
age = 18
print(f'my name is {name}, age is {age}')
open()