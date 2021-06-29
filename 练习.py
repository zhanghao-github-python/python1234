# 打印9*9矩形
# i = 1
# while i<=9 :
#     print("*********")
#     i +=1
a = 1
# while a<=9 :
#     b=1
#     while a<=9 :
#         print("*", end="")
#         b +=1
#     print("")
#     i +=1
#
#
# str = "ab,cd,ef"
# print(id(str))
# str= str.replace("a","A")
# print(str)
# print(str.split("b"))
# print(str.find(","))
#

# nums=list(range(1,101))
# print(nums)
# nums=list(range(1,101,2)) #取奇数
# print(nums)
# nums=list(range(2,101,2)) #取偶数
# print(nums)
# nums=list(range(1,101))
# print(nums)
# print(nums[99])
# food = [["湖南", "糖油粑粑", [10,"五个一份"]],["湖北","热干面",[6,"管饱"]],["广东","肠粉",[8,"不管饱"]],["河南","胡辣汤",[4,"喝不饱"]]]
#
# print(food)
# food.insert(0,"a")
# print(food)
# print(food)
# food.remove("a")
# print(food)
# print(len(food))
# print(max(food))
# print(min(food))
# str=[1,2,3,4,5]
# print(type(str))
# str.reverse()  #反转
# print(str)
# str.sort()   #从小到大
# print(str)
# str.sort(reverse=True)      # 从大到小
# print(str)
# str = (0,1,2,3,4,5)
# str=list(str)
# str[5]=6
# print(str)
# str=tuple(str)
# print(type(str))
# print(max(str))
# print(min(str))
# print(len(str))
# student = {"name":"张浩","age":25,"height":180,"weight":"77kg"}
# print(student["name"])
# student.pop("weight")
# print(student)
# student["age"]= 27
# print(student)
# student["weight"]= "80kg"
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())


# age = int(input("请问您的年龄是:"))
# # beer=1 #带了酒水
# # if age>=18 :
# #     print("欢迎光临魅力四射酒吧")
# #     print("请过安检")
# #     if beer==0 :
# #         print("本店禁止自带酒水，我帮您保管！")
# #     else :
# #       print("安检通过")
# # else :
# #     print("未成年人禁止入内，回家洗洗睡吧！")
# print("欢迎使用它石牌BMI计算器！")
# # weight = float(input("请输入您的体重(kg):"))
# # height = float(input("请输入您的身高（m）:"))
# # BMI = round(weight/(height**2),1)
# # if BMI<=18.4 :
# #     print("您的体重偏瘦，请多吃点~")
# # elif 18.4<=BMI<=23.9:
# #     print("您的体重正常，请继续保持！")
# # elif 24.0<=BMI<=27.9 :
# #     print("您的体型[肥胖]，请少吃饭")
# # elif BMI>=28.0 :
# #     print("您的体重超标,建议您绝食")
# # else :
# #     print("您的输入有误，请重新输入！！！")
# import requests
# # login_data= {"username":"zhanghao1324","email":"769421356@qq.com","password":"123456","confirm_password":"123456",
# #              "extend_5":"13997821732","sel_question":"favorite_novel","password_answer":"北辰","agreement":"1","act":"act_register"}
# # login_url="http://192.168.11.3:81/ecshop/user.php?act=register"
# # r=requests.post(login_url,data=login_data)
# # print(r.status_code)
# # result=r.text
# # print(r.text)
# # if result.find("注册成功")!=-1:
# #     print("注册成功")
# # else :
# #     print("注册失败")
    #================================================
# import requests
# s=requests.session()   # 用session建立连接
# login_data = {"username":"zhanghao1324","password":"123456","act":"act_login"}
# login_url = "http://192.168.11.3:81/ecshop/user.php"
# r=s.post(login_url,data=login_data)
# print(r.status_code)     #打印响应代码
# result = r.text       #查看响应文本
# if result.find("登录成功")!=-1:
#     print("登录成功")
# else:
#     print("登录失败")
# data={"amount":"1000","user_note":"tashi5","payment_id":2,"act":"act_account"}
# url = "http://192.168.11.3:81/ecshop/user.php"
# r=s.post(url,data)
# if r.text.find("您的充值金额为")!=-1:
#     print("充值成功")
# else :
#     print("充值失败")

# """
#
#
# ewqffdge
# """
# print("===============")
# print(int(10/3))
# print(type(10%3))
# print(10//3)
# print(type(10//3))
# str = "helloword"
# print(str[::2])
# name = "张浩"
# age = 15
# weight= 75.05
# print("他叫%s,他的年龄是%d,他的体重是%.2f" %(name,age,weight))
# str = "ab,cd,ef"
# str=str.replace("a","A")
# print(str)
# # str.split("Ab")
# # print(str.split("Ab"))
# str.find("Ab")
# print(str.find("Ab"))
# nums=list(range(1,101,2))
# print(nums)
# nums1=list(range(2,101,2))
# print(nums1)
# import json
# student='{"username":"zs"}'
# print(type(student))
# student=json.loads(student)     #转换成字典
# print(type(student))
# print(student)
# student=json.dumps(student)    #转换成json类型字符串
# print(type(student))
# print(student)
#
# nums = list(range(-100,-1,2))
# print(nums)
#==================求1-2+3-4+5-6........-100的结果
# s=0
# for i in range(1,101,2) :
#     s +=i
# print(s)
# l=0
# for i in range(2,101,2):
#     l+=i
# print(l)
# print(s-l)
#
# l=0
# s=0
# for i in range(1,101) :
#     if i%2!=0:    # 奇数
#
#         s +=i
#     else :   #偶数
#
#         l+=i
# print(s-l)
# s=list(range(1,101,2)) + list(range(2,101,2))
#
# print(s)
# nums=[1,2,3,4]
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and j!=k and i!=k:
#                 print(i,j,k)
# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
# I = float(input("请输入利润I:"))
# print(str)
# if I>=10 :
#     print(I*0.1)
# elif 10<I<20 :
#     print(I*0.1+((I-10)*0.075))
# elif 20<=I<=40 :
#     print()
# !/usr/bin/python
# # -*- coding: UTF-8 -*-

# i = int(input('净利润:'))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for idx in range(0, 6):
#     if i > arr[idx]:
#         r += (i - arr[idx]) * rat[idx]
#         print(i - arr[idx]) * rat[idx]
#         i = arr[idx]
# print(r)
# for i in(1,85) :
#     for j in(2,85):
#         if j>=2 and 1<i<85 and j*i==168 and  :
#          print(i)
# for i in range(1,85):
#     if 168 % i == 0:
#         j = 168 / i;
#         if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)

# ste={'1':2,'3':4}
# print(type(ste))
# ste['1']  += 1
# print(ste)
# print(ste['1'])
# 定义一个函数将列表中的偶数提取出来并且放到另外一个列表中，数字不重复
# def Ser(num):
#     num1=[]
#     for i in num :
#         if  i%2==0 and i not in num1 :
#             num1.append(i)
#     return num1
# num2=[1,2,3,4,5,5,6,6,1,7]
# print(Ser(num2))
# import random
# c=random.randint(10000000,99999999)
# print(c)
# import os
# index = os.urandom(2)
# print(index)

print("欢迎使用张浩牌憨憨判断器！")
name = str(input("请输入您的姓名(字符):"))
area = str(input("请输入你的家乡省份："))
if name == '周晨' and area == "甘肃省" :
       print("周晨，你是个憨憨")
else :
    print("你是个聪明的娃儿")

# - *- coding: utf-8 -*-
"""
========================================================
Author : ${USER}
Created on: ${DATE}

E-mail : 769314439@qq.com 

========================================================
"""