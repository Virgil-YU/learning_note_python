"""
格式化字符串除了%s，还可以写为f"{表达式}"

"""
age = 18
name = "tom"
weight = 22.5
stu_id = 1
stu_id1 = 100000
# 我的名字是x，今年x岁了
# 语法 f"{表达式}"
print(f"我的名字是{name}，今年是{age}岁了")  # f格式化字符串更加高效(python3.6)
