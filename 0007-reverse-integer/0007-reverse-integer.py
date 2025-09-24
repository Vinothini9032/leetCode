class Solution:
    def reverse(self, x: int) -> int:
        int_max=2**31-1
        int_min=-2**31
        rev=0
        sign=1 if x>0 else -1
        x=abs(x)
        while x!=0:
            d=x%10
            x//=10
            if rev > (int_max-d)//10:
                return 0
            rev=rev*10+d
        return sign*rev        