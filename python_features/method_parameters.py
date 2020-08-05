class MethodPara:
    def __init__(self, val: list):
        super().__init__()
        self.val = val
    
    def testPara(self, args: list):
        """Receives a list parameter.
        """
        print("testPara")
        for i, j in zip(self.val, args):
            print(i, j)
    
    def testParaVar(self, *args):
        """可变参数方法

        可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
        """
        print("testParaVar")
        for i, j in zip(self.val, args):
            print(i, j)

    def testKeywordPara(self, key1, key2, **kw):
        """关键字参数方法
        
        关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
        """
        print("testKeyWordPara")
        print("key1=",key1, "key2=", key2, "keywords=", kw)

    def testNamedKeywordPara(self, key1, key2, *, key3, key4):
        """使用命名关键字参数限制传入的关键字名

        * 之后的视为关键字参数

        若方法中已经定义了一个可变参数，它之后的参数会被视为命名关键字参数
        >>> testNamedKeywordPara(self, key1, *keys, key2, key3):
        """
        print("testNamedKeywordPara")
        print("key1=", key1, "key2=", key2)
        print("key3=", key3, "key4=", key4)

    def testCombinedPara(self, key1, *args, **kw):
        """位置参数，可变参数，关键字参数的组合
        """
        print("testCombinedPara")
        print("key1=", key1)
        for i in args:
            print(i, end=", ")
        print("\nkw=", kw)


def main():
    case = MethodPara([0,1,2,3,4,5,6,7,8])
    seq = [1,2,3,5,7,11,13,17,19,23]

    # 传统方法
    case.testPara(seq)
    
    #* 直接在参数中输入多个变量或值，可变参数可以将其作为一个可迭代对象处理
    case.testParaVar(1,2,3,5,7,11,13,17,19,23)

    #* 或者使用 * 来将列表或者元组的元素作为可变参数处理
    case.testParaVar(*seq)

    #* 传入关键字参数
    case.testKeywordPara("val1", "val2", key3="val3", key4="val4")

    #* 命名关键字参数在传参时需要传入参数名，否则报错
    case.testNamedKeywordPara("val1", "val2", key3="val3", key4="val4")

    #* 多种传参方式组合
    case.testCombinedPara("val1", *["val2", "val3", "val4"], key5="val5", key6="val6")


if __name__ == "__main__":
    main()