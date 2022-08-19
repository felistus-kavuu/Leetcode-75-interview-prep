class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far, max_profit= float('inf'),0
        
        for i in range (0,len(prices)):
            profit_if_sold_today= prices[i]- min_price_so_far
            max_profit= max(profit_if_sold_today, max_profit)
            min_price_so_far= min(prices[i], min_price_so_far)

        
        return max_profit
