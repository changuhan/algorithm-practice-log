class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_price = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                current_price = prices[j] - prices[i]
                
                max_price = max(current_price, max_price)

        return max_price