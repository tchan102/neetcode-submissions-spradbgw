class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        maxProfit = 0
        for price in prices[1:]:
            if price < low: 
                low = price
            
            maxProfit = max(maxProfit, price - low)
        return maxProfit