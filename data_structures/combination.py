from typing import List

class Combination:
    """Contains some combination algorithms.
    """

    @staticmethod
    def fullCombination(nums: List) -> List[List]:
        """Full combination of the input sequence.

        Bit mask method.

        Args:
            nums: Input sequence.

        Returns:
            Full combination including empty set.

        Reference: 
            http://wuchong.me/blog/2014/07/28/permutation-and-combination-realize/
        """
        #* 使用二进制位的迭代来代表对应元素是否在组合中存在
        res = [] # 不需要提前加入空集

        bitmask = 1 # 用来判断对应数字是否加入的掩码
        iter_times = bitmask << len(nums) # 循环截止的上限值

        for i in range(iter_times): # 迭代从 0 开始则第一个加入的是空集
            temp = []
            for j in range(len(nums)): # 在给定元素数量内循环检测每一位是否要加入
                if (1 << j) & i: # 若对应位和掩码与结果不为 0 则加入
                    temp.append(nums[j]) 
            res.append(temp)
        return res

    @staticmethod
    def ZuHeIndex(li):
        """Another method for creating combination

        Reference:
            From comment in https://blog.csdn.net/destiny_python/article/details/77461518
        """
        reli = []
        for i in range(0, len(li)):
            if 0 == i:
                reli.append([i])
            else:
                addli = []
                addli.append([i])
                for ii in reli:
                    addli.append(ii+[i])
                reli += addli
        return reli


def main():
    res = Combination.fullCombination(["a", "b", "c"])
    print(res)

if __name__ == '__main__':
    main()