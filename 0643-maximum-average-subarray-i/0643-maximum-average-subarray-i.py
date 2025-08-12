class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        maxi=0
        for r in range(k):
            sum+=nums[r]
        maxi=sum
        for i in range(k,len(nums)):
            sum+=nums[i]-nums[i-k]
            maxi=max(maxi,sum)
        return maxi/k
        
        