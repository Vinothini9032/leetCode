class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        res=None
        for i in nums:
            if count==0:
                res=i
                count=1
            elif i==res:
                count+=1
            else:
                count-=1
        return res