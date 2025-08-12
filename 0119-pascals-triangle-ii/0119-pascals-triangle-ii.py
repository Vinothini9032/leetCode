class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lis=[1]
        for i in range(1,rowIndex+1):
            lis.append(lis[-1]*(rowIndex-i+1)//i)
        return lis

           

           


        