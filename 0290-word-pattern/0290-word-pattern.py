class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w=s.split()
        if len(pattern)!=len(w):
            return False
        hashmap,has={},{}
        for c,e in zip(pattern,w):
            if c in hashmap and hashmap[c]!=e:
                return False
            if e in has and has[e]!=c:
                return False
            hashmap[c]=e
            has[e]=c
        return True
        