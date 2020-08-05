import math

class Anonymous:
    def __init__(self, val):
        super().__init__()
        self.val = val

    def testAnonymous(self):
        """使用 lambda 创建匿名函数

        格式：lambda [arg1, [args2, ... argsn]]: expression

        返回值为一个函数对象，通过引用这个对象可以调用匿名函数 
        >>> f = lambda x: x + 1
        >>> f(1)
        >>> 2

        或者使用括号将表达式及其参数分别括起来，直接运行表达式
        >>> (lambda x: x + 1) (2)
        >>> 2
        """
        # 将表达式命名并引用
        af = lambda val: val**2 
        print(af(2))

        # 直接运行表达式
        print((lambda x, y: math.sqrt(x**2 + y**2))(3, 4))


def main():
    case = Anonymous(0)
    case.testAnonymous()

if __name__ == "__main__":
    main()