class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d={}
        d1={}
        for num in nums1:
            d[num]=True
        for nums in nums2:
            d1[nums]=True
        d2=[]
        for i in d:
            if i not in d1:
                d2.append(i)
        d3=[]
        for j in d1:
            if j not in d:
                d3.append(j)
        return [d2,d3]

        
        