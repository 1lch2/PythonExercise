import sys
from io import StringIO

def io_sys_stdin():
    """标准输入流

    Ctrl + D 结束输入
    """
    for line in sys.stdin: # 按行分割输入
        s = line.split() # 该步返回一个 list，按空格分割元素
        print(s)

def io_input():
    """使用 input() 读取输入，会将输入内容作为表达式

    以换行符为结束标志

    Python 3 没有 raw_input() 方法，以 input() 代替
    """
    s = input()
    print(s)

def redirectStdin():
    """使用 StringIO 重定向标准输入
    """
    sys.stdin = StringIO("line1\nlin2\nlin3")

    for line in sys.stdin:
        s = line.split() # 会按照换行符分割，返回的是一个只含一个元素的 list 
        print(s)


if __name__ == "__main__":
    print("\ninput()")
    io_input()
    print("\nredirect stdin")
    redirectStdin()