class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={'}':'{',')':'(',']':'['}
        stack=[]
        for char in s:
            if char in hashmap:
                top=stack.pop() if stack else '#'
                if hashmap[char]!=top:
                    return False
            else:
                stack.append(char)
        return not stack
        