from typing import List

class Permutation:
    """Permutation algorithms.
    """

    @staticmethod
    def permutation(s: str) -> List[str]:
        """Full permutation of input string.
        """
        #*              "abc"
        #*            /   |   \
        #*           a    b    c
        #*          / \  / \  / \
        #*         b  c  a c a   b 
        #*         |  |  | | |   |
        #*         c  b  c a b   a
        if not s:
            return []

        res = [] # 存放返回结果
        used = [False for _ in range(len(s))] # 标记当前已访问过的元素

        def backtrack(path, selection):
            # 递归终止条件：剩余选项只有一个
            if used.count(False) == 1:
                path += selection[used.index(False)] # 将最后一个元素加入结果
                res.append(path) # 退出递归时将访问路径加入结果
                return
            # 遍历当前每一个可用选择
            for index in range(len(selection)):
                if used[index]:
                    continue

                used[index] = True # 进入递归前标记本次的选择
                path += selection[index] # 将选择加入路径
                backtrack(path, selection) # 进入递归

                path = path[:-1] # 从路径中移除本次加入的选择
                used[index] = False # 取消标记，进入下一轮迭代
        
        backtrack("", s)

        return list(set(res)) # 去重


def main():
    s = "aba"
    print(Permutation.permutation(s))

if __name__ == "__main__":
    main()