# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。
# 要求时间复杂度是O(n)，空间复杂度是O(1)。

# 示例 1：
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]

# 示例 2：
# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]

# 限制：
# 2 <= nums.length <= 10000

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 对所有数字异或得到 a，b两数的异或结果
        xor = 0
        for i in nums:
            xor = xor ^ i
        
        # 取异或后最后一个为 1 的位
        # 因为异或结果为 1 的位在两数上必不相同
        # 因此可以按照该位来对所有数字进行分组
        mask = 1
        while xor & mask == 0:
            mask = mask << 1
        
        # 按照与 mask 的异或结果分组进行异或
        m, n = 0, 0
        for i in nums:
            if i & mask == 0: # 此处不能以 1 来判断，结果只能为 0 或者 mask
                m = m ^ i
            else:
                n = n ^ i
        return [m, n]