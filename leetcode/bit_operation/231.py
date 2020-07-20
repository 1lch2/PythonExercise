# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

# 示例 1:
# 输入: 1
# 输出: true
# 解释: 20 = 1

# 示例 2:
# 输入: 16
# 输出: true
# 解释: 24 = 16

# 示例 3:
# 输入: 218
# 输出: false

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
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

class Solution2:
    def isPowerOfTw0(self, n: int) -> bool:
        #* n & (n-1):   n 最右侧的 1 变为 0
        #* 若为 2 的 n 次幂， 只有一个 1

        if n == 0:
            return False
        return n & (n-1) == 0
