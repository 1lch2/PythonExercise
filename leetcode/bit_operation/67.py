# 给你两个二进制字符串，返回它们的和（用二进制表示）。

# 输入为 非空 字符串且只包含数字 1 和 0。

# 示例 1:
# 输入: a = "11", b = "1"
# 输出: "100"

# 示例 2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"

# 提示：
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Do not use int()
        a = self.binStr2int(a)
        b = self.binStr2int(b)

        return self.int2binStr(a+b)
    
    def binStr2int(self, n: str) -> int:
        res = 0
        for i, j in zip(range(len(n)-1, -1, -1), range(len(n))):
            res += int(n[i]) * (2 ** j)
        return res
    
    def int2binStr(self, n: int) -> str:
        res = []
        if n == 0:
            return "0"

        while n != 0:
            res.insert(0, str(n & 1))
            n  = n >> 1
        return "".join(res)
        
class Solution0:
    # https://leetcode-cn.com/problems/add-binary/solution/er-jin-zhi-qiu-he-by-leetcode-solution/
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y  # 计算 x 和 y 的无进位相加结果

            #* x = 1010 1000 = 168
            #* y = 0111 0100 = 116
            #* x^y = 1101 1100 = 220
            #* x&y = 0010 0000
            #* x&y << 1 = 0100 0000 = 64

            carry = (x & y) << 1    # 计算 x 和 y 的进位
            x, y = answer, carry
        return bin(x)[2:]   # bin()返回一个字符串

if __name__ == "__main__":
    S = Solution()
    S_ = Solution0()

    print(S.addBinary("0", "0"))
    print(S_.addBinary("11", "1"))
