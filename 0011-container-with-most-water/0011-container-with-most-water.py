from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        while l<r:
            a=r-l#distance
            d=min(height[l],height[r])#value fill panna min value
            f=a*d ##area=length*breadth
            if f>res:
                res=f
            elif height[l]>height[r]:
                r-=1
            else:
                l+=1
        return res