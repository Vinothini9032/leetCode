class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lis=[[1]]
        for i in range(numRows-1):
            temp=[0]+lis[-1]+[0]
            temp_list=[]
            for j in range(len(temp)-1):
                temp_list.append(temp[j]+temp[j+1])
            lis.append(temp_list)
        return lis

        