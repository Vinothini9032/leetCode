class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=0
        r=0
        lis=[]
        while l<len(word1) and r<len(word2):
            lis.append(word1[l])
            lis.append(word2[r])
            l+=1
            r+=1
        if l<len(word1):
            lis.append(word1[l:])
        if r<len(word2):
            lis.append(word2[r:])
        return "".join(lis)