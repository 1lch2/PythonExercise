# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 示例 1:
# 输入: "()"
# 输出: true

# 示例 2:
# 输入: "()[]{}"
# 输出: true

# 示例 3:
# 输入: "(]"
# 输出: false

# 示例 4:
# 输入: "([)]"
# 输出: false

# 示例 5:
# 输入: "{[]}"
# 输出: true

# From top comment
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "") 
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        return s == ""

# From official solution
class Solution2:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False

        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # 若char为右括号
            if char in mapping: 
                # 若栈非空则弹栈，否则添加伪元素充数
                top_element = stack.pop() if stack else '#'
                # 若遇到右括号时，栈顶括号不匹配
                if top != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0
