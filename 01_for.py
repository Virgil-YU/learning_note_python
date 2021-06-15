"""
for语法：
    for 临时变量 in 序列:
        重复执行的代码

"""

"""
准备一个数据序列

"""
# str2 = "ni hao a"
# for i in str2:
#     print(i, end=" ")
# break测试&continue测试
str2 = "ni hao a"
for i in str2:
    if i == " ":
        continue
    print(i, end=" ")
print("不打印空格")
