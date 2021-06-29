#打印99乘法表
# i = 1
# while i <= 9 :
#     j=1
#     while j<=i :
#         print("{}*{}={}".format(j,i,j*i),end=("\t"))
#         j +=1
#     print("")
#     i +=1
# print("="*100)
# for i in range(1,10) :
#     for j in range(1,i+1) :
#         print("{}*{}={}".format(j,i,j*i),end="\t")
#     print("")
# #生成偶数列表
# nums=list(range(2,101,2))
# print(nums)
#输入用户名/密码验证
# username = input("请输入您的用户名:")
# password= input("请输入您的密码:")
# if username=="张浩" and password=="123456" :
#     print("登录成功")
# else :
#     print("登录失败")
# 打印十次中国很强
# i=1
# while i<=10 :
#     print("中国很强")
#     i+=1
#用函数 求1-n的奇数和
# def sum(n) :
#     j=0
#     for i in range(1,n+1,2):
#         j +=i
#     return j
# print(sum(5))
#==========斐波那契数列==========
# a,b=0,1
# # nums=[]
# # for i in range(1,25) :
# #     nums.append(b)
# #     a,b=b,a+b
# # print(nums)
#===========统计字符串的长度====
# str = input("请输入你要统计的字符串:")
# s = 0
# for i in str :
#     s +=1
# print("您要统计的字符串长度为{}".format(s))
#===========统计字符串中字母和数字的个数============
# str= input("请输入你要统计的字符串:")
# s=0
# l=0
# for i in str :
#     if i.isdigit():
#         s +=1
#     elif i.isalpha():
#         l +=1
# print("您要统计的字符串中数字有{}个,字母有{}个".format(s,l))
#==============输入任意5个整数,从小到大排序================
# nums=[]
# for i in range(1,6) :
#      num=int(input("请输入第{}个整数:".format(i)))
#      nums.append(num)
#      nums.sort()
# print(nums)
# f= open("tashi111.txt",mode="w")
# f.write("123")
# f= open("tashi111.txt","a")
# f.write("12345")
# f= open("tashi111.txt","r")
# # print(f.read())
# # f.close()  # 关闭文件
# # print(f.closed)  #验证文件是否关闭
# print(f.readline())   #每次读取一行
# print(f.readline())
# print(f.readlines())  #读取所有
#===============备份文件名字================
old = input("请输入您要备份的文件名:")
dian = old.find(".")
print(dian)
a=old[:dian]
b=old[dian:]
new = a+"-副本"+b
with open(old)  as f:
    c=f.read()
with open(new,"w") as f:
    f.write(c)
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

# =================conding: utf-8
"""
================================================================================

Author : ${USER}
Created  on : ${DATE}

E-mail: zh13997821732@163.com


================================================================================

"""
print('nihao')