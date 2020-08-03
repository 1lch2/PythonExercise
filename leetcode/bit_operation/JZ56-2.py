# 在一个数组 nums 中除一个数字只出现一次之外，
# 其他数字都出现了三次。
# 请找出那个只出现一次的数字。

# 示例 1：
# 输入：nums = [3,4,3,3]
# 输出：4

# 示例 2：
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1

# 限制：
# 1 <= nums.length <= 10000
# 1 <= nums[i] < 2^31

from typing import List

# LeetCode 137
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0 for x in range(32)] # 记录32位里每一位 1 出现的次数
        for num in nums:
            j = 0
            while j < 32: # 对一个数字进行32位循环右移，给对应出现 1 的位加 1
                bits[j] += num & 1
                num = num >> 1
                j += 1
        
        res = 0
        for i in range(32):
            bits[i] %= 3 # 对每一位的 1 的数量求 3 的模
            res += bits[i] * (2**i) # 累加将二进制转为十进制
        return res

if __name__ == "__main__":
    S = Solution()
    print(S.singleNumber([2,3,3,3]))
    print(S.singleNumber([1,3,3,3,4,4,4]))