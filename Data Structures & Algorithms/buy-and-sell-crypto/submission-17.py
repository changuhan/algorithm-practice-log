class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        largest = 0
        

        for price in prices:
            lowest = min(lowest, price)
            price = price - lowest
            largest = max(largest, price)


        return largest