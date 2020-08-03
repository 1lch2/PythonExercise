# 给定两个整数，被除数 dividend 和除数 divisor。
# 将两数相除，要求不使用乘法、除法和 mod 运算符。

# 返回被除数 dividend 除以除数 divisor 得到的商。

# 整数除法的结果应当截去（truncate）其小数部分，
# 例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

# 示例 1:
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

# 示例 2:
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2

# 提示：
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        res = 0 # 移位次数和
        # 判断结果是否为负
        # 两数异或计算，结果为负则为两数异号
        negetive = (dividend ^ divisor) < 0

        # 取绝对值计算
        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0

        while True:
            k = divisor # 保存除数副本
            i = 0 # 记录左移次数
            while (k << 1) < dividend:
                k = k << 1
                i += 1
            res += (1 << i) # 此处加上除数左移次数的 2 的幂，即乘法的因数
            dividend -= k

            if dividend < divisor: # 当被除数已经不能再减去除数的整数倍时
                if negetive:
                    return -res
                else:
                    # 处理溢出
                    if res > (2**31 - 1):
                        return 2**31 -1
                    else:
                        return res

if __name__ == "__main__":
    S = Solution()
    print(S.divide(-2147483648, -1))
    print(S.divide(10, 3))
    print(S.divide(-7, 2))
    print(S.divide(-10, -1))