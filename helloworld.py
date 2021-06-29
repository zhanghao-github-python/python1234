# print('helloworld')  # 打印helloworld
# '''
# 1
# 2
# '''
# ''''''
# 2
# 1
# ''''''
#
# print(type(0))
# print(type(-1))
# print(type(1))
# print(type("abc"))
# print(type(''))
# print(type(True))
# print(type(False))
# print(type(None))
# print(type(-1.1))
# print(type(2.2))
# print(type(0.0))
# print(type(1.0))
# print(type(True))
# print(type("12345"))
# st = True
# print(st)
# import keyword
# print (keyword.kwlist)
# teacher = "郭老师" # 区分大小写
# Teacher = "许老师"
# student2_a = "123"
# print(teacher)
# print(student2_a)
# print(Teacher)
# c, d = 3, 4
# print(c, d)
# e = f = 3
# print(e, f)
# c = 8
# print(c)
# num1, num2 = 2, 3
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(int(10 / 3))
# print(int(10 // 3))
# print(int(10 % 3))
# print(10 / 3)
# print(3**3)
# print("张" + "李家辉")
# print(7**2)
# a=2
# a += 2
# print(a)
# b=3
# b -=3
# print(b)
# c=4
# c *=4
# print(c)
# d=4
# d /=2
# print(int(d))
# e=3

# print(True and True)  #两边为真 结果为真
# print(True and False)  # 一边为假， 结果为假
# print(True or False) # 一边为真，结果为真
# print(3>1 and 3<1 ) #为假
# print(not True)  #为假
# print(not False) # 为真
# print(3>1 or 3<1 )  # 为真
# print(not 3<1 )
# print(3>1)
# print(3>=1)
# # print(3<=1)
# # print(3<1)
# # print(3!=1)
# # print(3==1)
# # print(3==3)
# str = "helloworld"
# print(str[8])
# print(str[:])
# print(str[8:])
# print(str[5:])
# print(str[0:5])
# print(str[::1])
# print(str[::3])
# print(str[::4])
# print(str[::5])
# print(str[::7])
# print(str[0])
# print(str[-1])
# print(str[9])
# print("china is strong"" \n  ""china is strong")
# print("china is strong"" \t ""china is strong")
# print("china is strong"" \t ""china is strong")
# print("D:\n\t\a\a.txt")
# print("D:\\n\\t\\a\\a.txt") #加\取消特殊含义
# print(r"D:\n\t\a\a.txt")    # 字符串前面加r 取消特殊含义
# name =  "小红"
# age = 20
# money = 190.123
# height = "180.01"
# %s 字符串
# %d 整数
# %f 浮点 指定精度 .nf
# 使用百分号

# print("他叫%s, 他今年%d岁， 他身上有%.2f元钱" %(name, age, money))
# print("他叫{}, 他今年{}岁， 他身上有{}元钱" .format(name, age, money))
# print("他叫{0}, 他今年{1}岁， 他身上有{2}元钱， 我借给他{0}元钱, 他的身高为{3}厘米" .format(name, age, money, height))
# print("他叫{0}, 他今年{1}岁， 他身上有{2}元钱， 我借给他{0}元钱, 他的身高为{0}厘米" .format(name, age, money, height))
# username = input("请输入您的用户名：")
# print("您输入的用户名是：{} " .format(username))
# print(type(username))
# print(type(-1))
# print(type(0))
# print(type("我"))
# print(type(""))
# print(type(-1.1))
# print(type(2.2))
# print(type(0.0))
# print(type(None))
# print(type(True))
# print(type(False))
# import keyword
# print(keyword .kwlist)
# print(keyword.kwlist)
# print(keyword.kwlist)
# student1 = "张浩"
# print(student1)
# student2 , student3 ="张浩", "张士钦"
# print(student2, student3)
# student5=student6="李家辉"
# print(student5,student6)
# print(1+1)
# print(1-3)
# print(2*3)
# print(4/2)
# print(int(4/2))
# print(33//2)
# print(33%6)
# print(4**3)
# 复合赋值运算符
# a=3
# a +=4
# print(a)
# b=3
# b -=3
# print(b)
# a=3
# a*= 3
# print(a)
# print(3>=1 or 3<=1)
# print(3>=1 and 3<=1)
# print(not 3<3)
# print(True)
# print(not True)
# print(not False)
# student = """张"""
# student = "zhang"
# sutdent = 'zhang'
# zhang = '''zhang'''
# str = "HelloWorld"
# # print(str[-1])
# # print(str[0])
# # print(str[::3])
# print("D:\n\a\a.txt")
# print("D:\\n\\a\\a.txt")
# print(r"D:\n\a\a.txt")
# print("D\n\t\a.txt")
# print("D:\\n\\t\\a.txt")
# print(r"D:\n\t\a.txt")
# name = "张浩"  # %s 字符串
# age = 25 # %d 整数
# money = 1000.79 # %f  浮点
# height = "180cm"  # %s 字符串
# weight = "80kg"
# print("他的名字叫%s , 他今年%d岁， 他有%.2f元钱， 他的身高为%s, 他的体重为%s " %(name , age, money, height, weight) )
# print("他的名字叫{}， 他今年{}岁， 他有{}元钱， 他的身高是{}，他的体重为{}" .format(name, age,money, height, weight))
# username = input("请输入您的用户名：")
# print("您输入的用户名为：{}" .format(username))
#
# print("您输入的用户名为：%s" %(username))
# str=("abcd")
# print(id(str))
# str=str.replace('a', 'A')
# print(id(str))
# print(str)
# print(str.find("c"))
# print(str.split("A"))
# print(str.find("e"))
# names = []
# nums=[1, 2,3, 4]
# print(nums)
# print(type(nums))
# nums=list(range(1, 101))
# print(nums)
# nums=list(range(2, 101, 2))
# print(nums)
# food = [["湖南", "糖油粑粑", [10,"五个一份"]],["湖北","热干面",[5,"管饱"]], ["广东", "肠粉",[5,"不管饱"]]]
# print(food[0][2][0])#10块钱一份
# print(food[0][1][0])
# print(food[0][0][0],food[1][0][0])
# nums=[2,3,4,5,6,7]
# nums.append(8)
# print(nums)
# nums.insert(2,9)
# print(nums)
# nums.insert(2,9)
# print(nums)
# nums.pop()  #shanc
# print(nums)
# nums.pop(0)  # 删除第一个元素
# print(nums)
# nums.remove(9) # 删除 9这个元素，如果有2个9 只默认删除di一个
# print(nums)
# nums.insert(5,9)  #在索引为5的位置插入一个9
# print(nums)
# nums.remove(9)    #删除列表中的第一个9
# print(nums)
# nums[4]= 8     #修改值，先用索引取值，再修改与索引对应的值
# print(nums)
# print(len(nums)) # 打印nums中元素的总数
# print(max(nums)) # 打印元素中的最大值
# print(min(nums)) # 打印元素中的最小值
# nums.insert(6,5) #在 索引为6的位置插入一个5
# print(nums)
# nums.reverse()  # 反转
# print(nums)
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
#类型转换，元组不能改
# nums = (1,2,3,4)
# print(type(nums))
# nums=list(nums)
# nums[3] = 5
# nums=tuple(nums)
# print(nums)
# print(type(nums))
#
# print(max(nums))
# print(min(nums))
# print(len(nums))
# student = {"name":"zs", "age":18, "tuition":True}  #定义一个字典
# print(student)
# print(type(student))
# student["name"] = "ljh" # 修改数据
# print(student)
# student.pop("age")  #删除数据
# print(student)
# student["height"] = 181  # 在字典中增加数据，字典中没有就自动加进去
# print(student)
# print(student.keys())  #获取所有的键
# print(student.values()) # 获取所有的值
# print(student.items())  #获取所有的键值对
# age = int(input("请问您的年龄是："))
# beer = 1
# if age>=18:
#     print("欢迎光临魅力四射酒吧！")
#     print("请过安检")
#     if beer==0:
#         print("我们店不允许带酒水")
#     else:
#         print("安检通过")
# else:
#     print("未成年人不允许进入，快点回去洗洗睡吧！")
# student = input("请问你是不是小学生：")
# if  student == "不是" :
#     print("一起来开黑吧！")
# else:
#     print("赶紧回家补作业！")
# print("欢迎使用它石牌BMI计算器~")
# weight = float(input("请输入您的体重(kg):"))
# height = float(input("请输入您的身高（m）:"))
# BMI = round(weight/(height**2), 1)
# if BMI<=18.4:
#     print("您的体型偏瘦，要多吃点~")
# elif 18.5<=BMI<=23.9:
#     print("您的体型正常，继续保持~")
# elif 24.0<=BMI<=27.9:
#     print("您的体型过重，请少吃点")
# elif BMI>=28.0:
#     print("您的体型[肥胖]，请绝食~")
# else:
#     print("您的输入有误，请重新输入")
# import random
# # player = int(input("请输入石头（0）剪刀（1）布（2）："))
# # computer = random.randint(0, 2)
# # if (player== 0 and computer==1) or (player==1 and computer==2) or (player==2 and computer==0) :
# #     print("恭喜您赢了游戏！")
# # elif player==computer :
# #     print("这局游戏平局")
# # else :
# #     print("不好意思你输了，菜逼，哈哈哈哈哈哈...")
# num = 1
# while num<=15 :
#     print(num)
#     num = num+1
# num=1
# while num<=100 :
#     if num%2 ==0 :  #打印1-100之间的偶数
#         print(num)
#     num +=1
#
# num=1
# while num<=100 :
#     if num%7==0 or str(num).find("7")==1 :
#         print(num)
#     num +=1
# a=1
# while a<=9:
#     b=1
#     while b<=9 :
#         print("*", end="") # end = ""的意思是不让它换行
#         b +=1
#     print("")  # 让它换行
#     a +=1
# a=1
# while a<=9:
#     b=1
#     while b<=a :
#         print("*", end="") # end = ""的意思是不让它换行
#         b +=1
#     print("")  # 让它换行
#     a +=1
# a=1
# while a<=9:
#     nt("")
#     a += 1
#     b=1
#     while b<=a :
#         print("{}*{}={}".format(b, a ,a*b), end="\t")
#         b +=1
#
# nums = "abdcd"
# # for i in nums :
# #     print("中国")
# # nums1=(1,2,3)
# # for i in nums1 :
# #     print(i)
# # nums2= [1,2,3,4,5]
# # for i in nums2 :
# #     print(nums2)
# # student={"name":"zs","age":18}
# # for i in student.keys():
# #     print(i)
# # for i in student.values() :
# #     print(i)
# # for i,j in student.items() :
# #     print("{}={}".format(i,j))
# for i  in range(1,101):
#     print(i)
# for i in range(1,101,2) :
#     print(i)
# for i in range(1,101) :
#     if i%7==0 :
#         print(i)
# for i in range(1,10) :
# #     print("********")
# # print("="*100)
# # for i in range(1,10):
# #     for j in range(1,10) :
# #         print("*",end=" ")
# #     print("")
# # print("="*100)
# # for i in range(1,10):
# #     for j in range(1,i+1):
# #         print("{}*{}={}".format(j,i,j*i),end="\t")
# #     print(" ")
# str= input("请输入需要统计长度的字符串:")
# num=0
# for i in str :
#     num +=1
# print("您输入的字符串的长度是:{}".format(num))
# num=0
# for i in range(2,101,2) :
#     num +=i  #内循环 取完再打印
# print(num)
# str = input("请输入您需要统计的字符串:")
# n = 0
# l = 0
# for i in str :
#     if i.isdigit():
#         n +=1
#     elif i.isalpha():
#         l +=1
# print("您查询的字符串中，字母有{}个，数字有{}个".format(l,n))


# ========斐波那契数列=================
# nums=[]
# a,b=0,1
# for i in range(1,13) :
#     nums.append(b)
#     a,b=b,a+b
# print(nums)
# def print_poetry() :
#     """打印古诗"""
#     print("锄禾日当午")
#     print("汗滴禾下土")
#     print("谁知盘中餐")
#     print("粒粒皆辛苦")
# for i in range(1,2) :
#     print_poetry()
# #
# help(print_poetry)  #  查看函数注释
# def add(a,b) :      #形参数
#     print(a%b)
# add(15,2)        #实际参数

# def sum(n) :
#     num = 0
#     for i in range(1,n+1,2) :
#         num +=i
#     print(num)
# sum(7)
# def add(a,b=3) :
#     print(a-b)
# add(b=5,a=5)
# add(9)
# add(10)
# def addd(a,b) :
#     print(123435)
#     return a+b
#     print(123435)
# print(addd(2,16))
# num1 = 199
# def add(a,b) :
#     print(num1)
#     global num2
#     num2=1999
#     return a+b
# print(add(2,10))
# print(num2)
# print("程序执行开始了")
# # print(d)
# try:
#     print(a)
# except Exception as f :
#     print("程序出现问题了,问题是:{}".format(f))
# else :
#     print("程序没问题")
# finally :
#     print("我始终会执行这个代码")
# print("程序执行结束")
# nums= int(input("请输入一个大于等于100的整数:"))
# if nums>=100:
#     print("输入成功")
# else:
#     raise Exception  ("您的输入有误")
# import time
# from time import ctime
# # print(time.cime())  # current
# print(ctime())
# 遍历字符串
# b= "qwdewfc3"
# for i in b :
#     print("中国很强")
# 遍历列表
# b = ["7u","1w","8u",3,"g",6,6]
# for i in b :
#     print(i)
# 遍历元组
# b=(1,2,3,4,5)
# for i in b :
#     print(i)
# 遍历字典
# student = {"name":"zs", "age":18}
# print(student.items())
# for i in student.keys() :
#     print(i)
# for i in student.values() :
#     print(i)
# for i in student.items() :
#     print(i)
# for a,b in student.items() :
#     print("{}={}".format(a,b))  # 使得键=值
# for i in range(1,101) :
#     print(i)
# for i in range(2,101,2) :
#     print(i)
# a=list(range(1,101))
# print(a)
# for i in list(range(1,101)) :
#     if i%4==0 and a.find==-1 :
#        print(i)
# num=1
# while num<=100 :
#     if num%4==0 or str(num).find("4")!=-1 :
#         print(num)
#     num +=1
# i=1
# for i in range(1,10) :
#     for j in range(1,i+1) :
#         print("{}*{}={}".format(j,i,j*i),end="\t")
#     print("")
# print("="*100)
#
# i=1
# while i<=9 :
#     j=1
#     while j<=i :
#         print("{}*{}={}".format(j,i,j*i),end="\t")
#         j +=1
#     print("")
#     i +=1
# i=1
# while i<=9 :
#     j=1
#     while j<=i :
#         print("{}*{}={}".format(j,i,j*i),end="\t")
#         j +=1
#     print("")
#     i +=1
# num = 0
# str=input("请输入需要统计的字符串:")
# for i in str :
#     num +=1
# print("字符串长度为{}".format(num))
# print(num)
# s = 0
# for i in range(2, 101, 2):
#     s += i
# print(s)
# str = input("请输入需要查询的字符串：")
# n = 0
# l = 0
# for i in str:
# # if i in '1234567890':
# if i.isdigit():
#     n += 1 # elif i in 'abcdefghijklmnopqrstuvwxyz': elif i.isalpha(): l += 1 print("您查询的字符串中，字母有{}个，数字有{}个".format(l, n))
# num=[]
# a,b=0,1
# for i in range(1,13) :
#     num.append(b)
#     a,b=b,a+b
# print(num)

# num = int(input("请输入一个大于等于100的整数："))
# if num>=100:
#     print("输入成功")
# else:
#     raise Exception("您的输入有误！")

# try:
#     print("a")
# except Exception as e:
#     print("程序出现问题啦，问题是：{}".format(e))
# else:
#     print("程序没有问题")
# finally:
#     print("我始终都会执行")
# print("程序执行结束")
# import time
# print(time.ctime())
# from time import ctime  #精准导入
# print(ctime())
# import time
# print(time.ctime())
# # time.sleep(10)
# print(time.strftime("%Y\%m-%d %H:%M:%S" ))
# nums=[]
# for i in range(1,6) :
#     num=int(input("请输入您第{}个整数:".format(i)))
#     nums.append(num)
#     nums.sort()
# print(nums)
# import os
# # os.mkdir("test")
# # os.rmdir("test")
#
# print(os.getcwd())
# import json
# # student = '{"name":"zs","age":18}'
# # student_dict=json.loads(student)  #将字符串类型的json数据转换成dict
# # student
# f = open("tashi.txt",mode='a')  # 追加append
# f.write("ab222c")
# f= open("addd.txt",mode="r")
# # f= open("addd.txt",mode="w")  # 创建
# f = open("tashi.txt",mode='r')  # 读，代码执行后不显示文件里面的东西
# f2 = open("tashi.txt")
# # print(f2.read())
# # print(f2.read(2))
# # print(f2.read(2))
# print(f2.readline())  #读取第一行
# print(f2.readline())   #连续读取的话，读取第二行数据
# print(f2.readlines())
# f2.close()
# print(tashi.txt)
# f = open("tashi1.txt",mode="w",encoding="utf8")
# f.write("china is strong\n中国很强")
# f.close()
#读取
# f2=open("tashi1.txt",encoding="utf8")
# print(f2.read())
# f2.close()
# with open("tashi1.txt",mode="r",encoding="utf8") as f :
#     print(f.read())
# print(f.closed)
# str=input('请输入一个文件名:')
# with open("{}".format(str)) as e :
#      with open("{}-副本".format(str),mode="w" ,encoding="utf8" )as f:
#          f.write(e.read())

# def sum(n) :
#     j=0
#     for i in range(0,n+1,2) :
#         j+=i
#     return j
# print(sum(10))
# old = input("请输入需要备份的文件名:")
# dian = old.find(".")
# print(dian)
# a=old[:dian]
# b=old[dian:]
# print(a)
# print(b)
# new = a+"-副本"+b
# with open(old) as f:
#     c = f.read()
# with open(new,mode="w") as f :
#     f.write(c)
# class Dog:
#     def __init__(self,color,weight):
#         self.color=color
#         self.weight = weight
#
#     def eat(self):
#         print("{}的狗在吃屎".format(self.color))
#     def sleep(self):
#         print("{}斤重的狗在睡觉".format(self.weight))
# # wangcai = Dog("黑色",50)
# # wangcai.eat()
# # wangcai.sleep()
# class jinmao(Dog):
#     def eat(self):
#         print("{}的狗在吃狗粮".format(self.color))
#     def chaijia(self):
#         print("他正在拆家")
#     def sleep(self):
#         print("{}斤重的狗在睡觉".format(self.weight))
# shamao= jinmao("黄色",60)
# shamao.chaijia()
# shamao.eat()
# shamao.sleep()


# nums = list(input("请输入数字:"))
# print(nums)

a=[1,2,3,3,4,5,6,7]
nums=[]
for i in a :
    if i%2!=0 :
        nums.append(i)


print(nums)
with open("tashi1.txt","w")  as f :
    f.write(str(nums))
def s(list2) :

    list1=[1,2,3,3,2,1]
    list2=[]

    for i in list1:
     if i not in list2 and i%2==0 :

        list2.append(i)
     print(list2)
    return list2

