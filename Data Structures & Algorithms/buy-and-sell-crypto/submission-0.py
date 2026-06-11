class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = prices[0]
        max_profit = 0

        for i in prices[1:]:
            max_profit = max(max_profit, i - lowest)
            lowest = min(lowest, i)


        return max_profit