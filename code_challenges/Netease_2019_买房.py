# 在一条街上有n幢房子，标号从1到n，两个在标号上相差为1的房子视为相邻，这些房子中有k幢房子已有住户。
# 现你准备搬入这条街，你能搬入一幢房子的条件是这幢房子没有人住在里面，与此同时由于你非常热爱与邻居进行交流，故而你需要你所入住的房子两边上都有住户。
# 现要你求最小的可能符合要求的房子数，以及最大的可能符合要求的房子数。

# Note: 就样例来说，#代表已有住户，-代表空位，这种情况（###---)，没有满足条件的房子，为最小，故输出0
# 最大的情况为(#-#-#-)，此种情况有二个位置满足条件，为最大，故输出2

# 输入描述:
# 输入的一行为测试用例数t(1 <= t <= 200000)，

# 接下来t行，每行含两个整数n和k，(1 <= n <= 1,000,000,000，0 <= k <= n)

# 输出描述:
# 对于每个用例输出最小的可能数以及最大的可能数

# 输入例子1:
# 6
# 1 0
# 1 1
# 2 0
# 2 1
# 2 2
# 6 4

# 输出例子1:
# 0 0
# 0 0
# 0 0
# 0 0
# 0 0
# 0 2

import sys

def countPlace(full: int, one: int) -> int:
    if one < 2 or full - one < 1:
        return 0
    
    return min(full - one, one - 1)

# https://www.nowcoder.com/questionTerminal/edf9346066f047a9833b3284798d6c29?answerType=1&f=discussion
# https://www.nowcoder.com/test/question/done?tid=35625452&qid=353480#summary User: ElonB
if __name__ == "__main__":
    index = 0
    for line in sys.stdin.readlines():
        if index == 0:
            continue
        
        nums = line.split()

        #* min(n-k, k-1)
        big = countPlace(nums[0], nums[1])
        print(0, big)
        