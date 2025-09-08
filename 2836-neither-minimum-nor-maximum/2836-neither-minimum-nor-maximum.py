class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return -1
        min_ele=nums[0]
        max_ele=nums[0]
        for i in range(len(nums)):
            if nums[i]<min_ele:
                min_ele=nums[i]
            elif nums[i]>max_ele:
                max_ele=nums[i]
        for i in range(len(nums)):
            if nums[i]!=min_ele and nums[i]!=max_ele:
                return nums[i]
        return -1
        

        