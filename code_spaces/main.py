class Solution:
    def twoSum(self, nums: list(int), target: int):
        for i in range(len(nums) - 1):
            for j in nums[i:]:
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j]