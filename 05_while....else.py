"""

语法：
    while 条件：
        条件成立重复执行的代码
    else:
        条件代码
实现结果：while的内容执行完直到执行失败，返回执行else的内容（只会执行1次）
"""
# 需求：打印5遍hello，内容，完成后执行你好
# i = 0
# while i < 5:
#     i += 1
#     print("hello")
# else:
#     print("你好")

# while。。。else中break退出
i = 0
while i < 5:
    i += 1
    print("hello")
    if i ==3:
        print("已经三遍了")
        continue
else:
    print("你好")
