class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first=second=third=None
        
        for i in range(len(nums)):
            if nums[i]==first or nums[i]==second or nums[i]==third:
                continue
            if first is None or nums[i]>first:
                third=second
                second=first
                first=nums[i]
            elif second is None or nums[i]>second:
                third=second
                second=nums[i]
            elif third is None or nums[i]>third:
                third=nums[i]
        return third if third is not None else first