# 给你一个字符串 s，找到 s 中最长的回文子串。

# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。

# 示例 2：
# 输入：s = "cbbd"
# 输出："bb"

# 示例 3：
# 输入：s = "a"
# 输出："a"

# 示例 4：
# 输入：s = "ac"
# 输出："a"

# 提示：
# 1 <= s.length <= 1000
# s 仅由数字和英文字母（大写和/或小写）组成

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """动态规划解法

        状态 DP(i, j) 为从 i 到 j 的字符串是否为回文串，即 True 或 False。
        一个回文串 s[i:j] (包含j) 为回文串，当且仅但s[i] == s[j] 且去除两端字符后还为回文串。

        状态转移方程为：DP(i, j) = (s[i] == s[j]) & DP(i+1, j-1)。
        基本情况为：DP(i, j) = True, i = j
                            = True, s[i] = s[j] 且 i+1=j
        当 i < j 时为 False。

        时间复杂度：O(n^2)
        """
        length = len(s)
        # 使用起始点加长度来定位最长子串
        max_length = 1 
        start = 0

        # 长度小于2的字符串必定为回文串
        if length < 2:
            return s
        
        # 初始化状态表格
        dp = [[False for __ in range(length)] for _ in range(length)]

        # 填充状态表格
        # 对角线均为 True
        for i in range(length):
            dp[i][i] = True
        
        # 上三角，从上到下，从左到右填充
        for j in range(1, length):
            for i in range(j):
                # 填充 True 的情况
                if s[i] == s[j]:
                    # 基础情况：字符串长小于等于 3
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                
                # 记录当前最长字串及其长度
                if dp[i][j]:
                    current_max = j - i + 1
                    if current_max >= max_length:
                        max_length = current_max
                        start = i
        
        return s[start: start + max_length]
        