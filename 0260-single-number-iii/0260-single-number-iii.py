class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lis=[]
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        for i,num in enumerate(nums):
            if hashmap[num]==1:
                lis.append(num)
        return lis