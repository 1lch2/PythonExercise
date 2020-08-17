from typing import List

class Permutation:
    """Permutation algorithms.
    """

    @staticmethod
    def permutation(nums: list) -> List[List]:
        """Full permutation of input string.

        Assuming the input list is ordered.
        """
        #* 同一层之间迭代，不同层之间递归向下进入
        #      "112"
        #      / | \
        #    1   1   2
        #   / \     / \
        #  1  2    1   1
        #  |  |    |
        #  2  1    1
        if not nums:
            return []

        res = [] # 存放返回结果
        used = [False for _ in range(len(nums))] # 标记当前已访问过的元素

        def backtrack(path, selection):
            # 递归终止条件：剩余选项只有一个
            if used.count(False) == 0:
                res.append(path.copy()) # 使用拷贝避免引用导致结果被修改
                return
                
            # 遍历当前每一个可用选择
            for index in range(len(selection)):
                # 若当前选项已被选择过则跳过
                if not used[index]:                
                # 若当前选择与上一轮选择的元素相同则跳过
                    if index > 0:
                        # index 下标无法区分不同递归，需要判断前一次是否被选择过
                        # 若相同元素在前一次递归被选择过则需要剪枝
                        # 使用跨越不同层递归的 used 来判断
                        if selection[index] == selection[index-1] and not used[index-1]:
                            continue
                    
                    used[index] = True # 标记本次使用的元素
                    path.append(selection[index]) # 加入路径
                    backtrack(path, selection) # 进入下一层递归

                    path.pop() # 去除本次加入的元素
                    used[index] = False # 取消标记
        
        backtrack([], nums)

        return res


def main():
    s = [1,1,2]
    print(Permutation.permutation(s))

if __name__ == "__main__":
    main()