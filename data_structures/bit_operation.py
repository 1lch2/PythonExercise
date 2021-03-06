class Bit:
    """Bit operation solutions
    """
    @staticmethod
    def getSmallest2Power(x: int) -> int:
        """For the given integer x, return the smallest power of 2 that bigger than x.
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

    @staticmethod
    def hammingWeight(n: int, method=0) -> int:
        """Count the number of 1 in the binary of input integer.

        Args:
            n: The input integer.
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

    @classmethod
    def reverseBits(cls, n: int) -> int:
        """Reverse a 32-bit unsigned integer.
        """
        res = 0
        power = 31 # 32位无符号整数
        while n != 0:
            #* n&1 取最右侧的位
            #* 左移 power 位将右侧的位换到左侧对称位置
            res = res | ((n & 1) << power)
            n = n >> 1
            power -= 1

        return res

    @classmethod
    def isPowerOfTwo(cls, n: int, method=0) -> bool:
        """Judge if the input integer is power of 2.

        Args:
            n: Integer.
            method: method=0: using complement code method.
                    method=1: using bit and method.
        Returns:
            Bool value.
        """
        if method==0:
            # 补码表示法中，x 与 -x 的共同点为最右侧符号相同
            #* e.g.:
            #* x补 = 15 = 0 0111
            #* -x补 = -15 = 1 1001
            #* x & (-x) = 0 0001 != x

            #* x补 = 16 = 0 1000
            #* -x补 = -16 = 1 1000
            #* x & (-x) = 0 1000 == x
            
            if n == 0:
                return False
            return n & (-n) == n
            
        elif method == 1:
            #* n & (n-1):   n 最右侧的 1 变为 0
            #* 若为 2 的 n 次幂， 只有一个 1

            if n == 0:
                return False
            return n & (n-1) == 0
        else:
            raise(ValueError("Invalid method number, should be 0 or 1."))

    @classmethod
    def isDivisible(cls, a: int, b: int) -> bool:
        """Judge if the input integer b can be divided by a.

        Args:
            a: The dividend
            b: The divisor
        
        Returns:
            Bool value.
        """
        #* 思路来源：github.com/LinkinYoung
        #* 若 a = kb，则可以将 k 转化为二进制
        #* a / b 的过程转化为 a 减去多个 k 的整数倍，直到 b 不再需要乘倍数
        #* 此时的结果为除法的余数，余数为 0 显然可以整除

        if a < b:
            return cls.isDivisible(b, a)
        
        while True:
            k = b # 保留除数的副本
            i = 0 # 记录左移次数
            # 对除数循环左移，直到高位在被除数高位的下一位
            while (k << 1) < a:
                k = k << 1
                i += 1
            
            a = a - k 
            if i == 0: # 左移次数为 0 时除法结束，此时检查余数是否为 0
                return a == 0 

    @classmethod
    def addWithoutSign(cls, a: int, b: int) -> int:
        """Calculate a + b without using "+"
        """
        #* ^ 异或，相当于无进位求和
        #* & 与，相当于求进位数
        #* 公式：(a ^ b) ^ ((a & b) << 1)
        #* 重复直到没有进位

        #* Python 中整数以补码形式存储

        x = 0xffffffff # 32位无符号整数
        a, b = a&x, b&x # 舍去32位以上的位数

        while b != 0: # 当进位数为 0 时跳出
            c = ((a & b) << 1) & x # 进位
            a = a ^ b # 无进位求和
            b = c# b 用进位数代替
        
        # 0x7fffffff 是最大的32位正整数
        if a <= 0x7fffffff:
            return a
        # 若结果为负数，则先将32位部分按位取反，再将整个数字取反
        # 结果为32位以内的不变，32位之外取反，得到负数
        else:
            return ~(a ^ x)


if __name__ == "__main__":
    print(Bit.getSmallest2Power(20))
    print(Bit.hammingWeight(15))
    
    print(bin(31))
    print(bin(Bit.reverseBits(31)))

    print(Bit.isDivisible(9, 3))
    print(Bit.isDivisible(9, 2))