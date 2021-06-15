"""
语法：
    for 临时变量 in 序列：
        重复的代码
    else：
        循环正常结束后要执行的代码
"""
str2 = "ni hao a"
for i in str2:
    print(i, end=" ")
else:
    print()
    print("循环正常结束")

# 配合使用break&continue（break是终止循环，else内容不执行，continue是少一次继续执行的）
str2 = "ni hao a"
for i in str2:
    if i == " ":
        print("已经三遍了")
        break
    print(i, end=" ")
else:
    print()
    print("循环正常结束")
