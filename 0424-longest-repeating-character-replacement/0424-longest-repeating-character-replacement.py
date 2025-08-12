class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        maxi=0
        max_len=0
        l=0
        for r in range(len(s)):
            count[s[r]]+=1
            maxi=max(maxi,count[s[r]])
            if (r-l+1)-maxi>k:
                count[s[l]]-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len