class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for char in s:
            hashmap[char]=hashmap.get(char,0)+1
        for char,i in enumerate(s):
            if hashmap[i]==1:
                return char
        return -1

        