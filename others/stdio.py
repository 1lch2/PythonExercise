import sys

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


if __name__ == "__main__":
    print("raw_input()")
    io_raw_input()
    print("\ninput()")
    io_input()