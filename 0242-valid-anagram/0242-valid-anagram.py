class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap,hashm={},{}
        for char in range(len(s)):
            hashmap[s[char]]=hashmap.get(s[char],0)+1
            hashm[t[char]]=hashm.get(t[char],0)+1
        return hashmap==hashm
           
        