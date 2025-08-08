class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s=set(jewels)
        hashmap={}
        for stone in stones:
            if stone in s:
                hashmap[stone]=hashmap.get(stone,0)+1
        return sum(hashmap.values())

        