# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，
# 表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；
# 输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，
# 所有的数字只表示重复的次数 k ，
# 例如不会出现像 3a 或 2[4] 的输入。

# 示例 1：
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"

# 示例 2：
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"

# 示例 3：
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"

# 示例 4：
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        # read into stack one by one
        while i < len(s):
            if s[i].isdigit():
                stack.append(s[i])
            elif s[i] == "[":
                stack.append(s[i])
            elif s[i].isalpha():
                stack.append(s[i])
            elif s[i] == "]": # build string from inside
                c = stack.pop()
                temp = []
                while c != "[":
                    temp.append(c)
                    c = stack.pop()

                # build multiplied string
                rev = self.reverse(temp)
                r = ""
                if c == "[":
                    # get multiple digits of numbers
                    num = []
                    while len(stack) != 0: # when the string is started with numbers
                        if stack[-1].isdigit():
                            num += stack.pop()
                        else:
                            break # jump out when numbers are collected
                    num = int(self.reverse(num))
                    for j in range(num):
                        r += rev
                # stack the string.
                stack.append(r)

            i += 1
        
        return "".join(stack)

    def reverse(self, s: list) -> str:
        res = ""
        for i in range(len(s)-1, -1, -1):
            res += str(s[i])
        return res

if __name__ == "__main__":
    s1 = "a3[b2[cd]e]f"
    s2 = "10[leetcode]"

    S = Solution()
    print(S.decodeString(s2))
