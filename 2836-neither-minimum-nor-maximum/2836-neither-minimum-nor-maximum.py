class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        return nums[1] if len(nums)>2 else -1
        

        