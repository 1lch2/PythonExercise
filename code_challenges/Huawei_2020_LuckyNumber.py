# 输入： 长度为 6 的数组，第一位为嘉宾，后面为五个参与抽奖者。
# 要求：每个字母对应的顺序值为幸运值，参与者的名字的幸运值加起来和嘉宾最接近的为中奖者
#     若有多个相同的，取最后一个
# 输出：中奖者的名字字符串

# 例：
# 输入：ccc aaa bbb abab cca bbe
# 输出：cca


import sys

def calculateLucky(names: list) -> int:
    # get letter to value map
    maps = {}
    for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
        maps[letter] = index + 1

    for index, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        maps[letter] = index + 1

    # calculate values
    val_list = []
    for name in names:
        val = 0
        for letter in name:
            if letter.isalpha():
                val += maps[letter]
        val_list.append(val)
    
    # get vip`s value
    vip_val = val_list.pop(0)

    delta_smallest = 65535
    index_smallest = -1

    for index, value in enumerate(val_list):
        delta = abs(value - vip_val)

        if delta <= delta_smallest:
            delta_smallest = delta
            index_smallest = index
    
    return index_smallest + 1
    

# Passes only 83.33% for unknown reasons
if __name__ == "__main__":
    # get input
    s = input()
    s = s.split()

    index = calculateLucky(s)
    print(s[index])