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
    def combination(selection: list, k: int) -> List[List[int]]:
        """Combination of given k number of elements.

        Args:
            selection: Available selection in ordered sequence. No repeated elements.
            k: Number of elements in each combination.
        
        Returns:
            All possible combination in a list.
        """
        if k < 1:
            return []
        if k > len(selection):
            raise ValueError("k is larger than the number of available elements.")

        res = [[]]

        def backtrack(start: int, path: list, selection: list):
            # 递归终止：path 已经有指定数量的元素k
            if len(path) == k:
                res.append(path[:]) # 使用拷贝避免引用导致结果被修改
                return
            
            # 遍历可用选择
            for i in range(start, len(selection)):           
                path.append(selection[i])

                # 排除本次选择元素，进入下一层递归
                backtrack(i+1, path, selection)

                path.pop() # 删除本次选择元素
        
        backtrack(0, [], selection)
        return res



def main():
    res = Combination.fullCombination(["a", "b", "c"])
    print(res)

    res = Combination.combination(["a", "b", "c"], 2)
    print(res)

if __name__ == '__main__':
    main()