https://leetcode.com/problems/best-time-to-buy-and-sell-stock

# O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_day_to_buy = 0
        best_day_to_sell = 0
        max_profit = 0

        for i in range(len(prices)):
            current_profit = prices[i] - prices[best_day_to_buy]
            if current_profit > max_profit:
                max_profit = current_profit
                best_day_to_sell = i
            
            if prices[i] < prices[best_day_to_buy]:
                best_day_to_buy = i

        return max_profit
