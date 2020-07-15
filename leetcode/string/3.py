# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l

        ch_set = set()
        right = -1 # Starts at the left of the left index
        length = 0

        # Move left index
        for i in range(l):
            # Skip the first iteration.
            if i != 0:
                ch_set.remove(s[i-1]) # Remove last character

            # Move the right index
            # Break the loop when encounters existing character.
            while right + 1 < l and s[right+1] not in ch_set: # Judge the NEXT character BEFORE entering the loop
                ch_set.add(s[right+1]) # Add next character
                right += 1

            # Get the maxmium length of sub-sequence.
            length = max(length, right - i + 1)
        
        return length