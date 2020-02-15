from typing import List

# Full permutation.
def permute(nums: List[int]) -> List[List[int]]:
    res = []
    temp_list = nums.copy()
    l_len = len(nums)

    def dfs(path, depth, length, res, queue, used):
        if depth == length:
            res.append(path.copy()) # Make a copy of `path` to prevent `res` from being changed when `path` changes.
            return 
        for i in range(l_len):
            if used[i] == False:
                used[i] = True
                path.append(queue.pop(0))

                dfs(path, depth+1, length, res, queue, used)

                used[i] = False
                queue.append(path.pop())
    
    used = [False for _ in range(l_len)]
    dfs([], 0, l_len, res, temp_list, used)

    return res


if __name__ == '__main__':
    sample = [1, 2, 3, 4]

    print(permute(sample))