class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 != 0:
            return True
        else:
            return False

# 如果堆中石头的数量 n 不能被 4 整除，那么你总是可以赢得 Nim 游戏的胜利。        