class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        mins=min(len(word) for word in strs)
        for i in range(mins):
            current=strs[0][i]
            for word in strs[1:]:
                if word[i]!=current:
                    return prefix
            prefix+=current
        return prefix    
        