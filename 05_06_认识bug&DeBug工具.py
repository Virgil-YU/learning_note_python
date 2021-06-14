"""
    bug 是程序中的错误

"""

# 类型1 ： NameError ：name is not define 未定义
# 类型2 ： IndentationError: unexpected indent 意外的缩进
# 类型3 ： NameError: name 'school_name' is not defined 变量先定义后使用

MyName = 'TOM'
print(MyName)

school_name = '黑马程序员'
print(school_name)

"""

    打断点，在左侧（如下）
    Debug 调试
    右键调试按钮
    按步执形快捷键：F8
    变量是临时存储在内存里的，调试执行完了，内存自然也就释放了；
    
"""
print(school_name)
