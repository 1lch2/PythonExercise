"""
Do not return anything, modify s in-place instead.
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        halflen = int(len(s)/2)
        for i in range(halflen):
            temp = s[i]
            s[i] = s[-(i+1)]
            s[-(i+1)] = temp