class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        rev="".join(reversed(s))
        for i in range(len(s)):
            if s.startswith(rev[i:]):
                return rev[:i]+s
        return s
        