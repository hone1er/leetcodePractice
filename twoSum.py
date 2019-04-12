class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target = target
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in nums and i != nums.index(needed):
                return [i, nums.index(needed)]