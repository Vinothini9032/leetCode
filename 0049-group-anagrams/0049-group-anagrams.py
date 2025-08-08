from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for char in strs:
            key=tuple(sorted(char))
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(char)
        return list(hashmap.values())


        