class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        for i,num in enumerate(nums):
            if hashmap[num]==1:
                return num