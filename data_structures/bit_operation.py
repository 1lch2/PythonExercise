class Bit:
    """Bit operation solutions
    """
    @staticmethod
    def getSmallest2Power(x: int) -> int:
        """Given integer x, return the smallest power of 2 that bigger than x.
        """
        i = 0
        # 先循环右移得到最高有效位
        while x > 0:
            x = x >> 1
            i += 1
        j = 1
        # 再循环左移得到次幂
        while i > 0:
            j = j << 1
            i -= 1
        
        return j

    @classmethod
    def hammingWeight(self, n: int, method=0) -> int:
        """Count the number of 1 in the binary of input integer.

        Args:
            n: Integer
            method: Different method. Can be 0 or 1:
        """
        count = 0

        if method == 0:
            # n 循环右移和 1 按位与
            while n != 0:
                count += n & 1
                n = n >> 1
        elif method == 1:
            # 统计 n 和  n-1 按位与得到 0 的次数
            #* n - 1 :      最右边的 1 变为 0 ， 此 1 右边的 0 都变为 1
            #* n & (n-1):   n 最右侧的 1 变为 0

            #* e.g.:
            #* n   = 1010 1000
            #* n-1 = 1010 0111
            #* n&(n-1) = 1010 0000

            while n != 0:
                n = n & (n - 1)
                count += 1
        else:
            raise(ValueError("Invalid method number, should be 0 or 1."))

        return count


if __name__ == "__main__":
    print(Bit.getSmallest2Power(20))
    print(Bit.hammingWeight(15))