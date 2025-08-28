class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        max_profit=0
        for i in range(len(prices)):
            mini=min(mini,prices[i])
            pro=prices[i]-mini
            max_profit=max(max_profit,pro)
        return max_profit