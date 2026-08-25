class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_profit=0
        min_price=float('inf')
        for i in range(n):
            min_price=min(prices[i],min_price)
            max_profit=max(prices[i]-min_price,max_profit)
        return max_profit
        


        