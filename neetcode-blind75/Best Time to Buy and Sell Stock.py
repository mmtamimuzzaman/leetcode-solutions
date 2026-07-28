class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        sell = prices[0]
        profit = sell - buy

        for price in prices[1:]:
            buy = min(buy,price)
            sell = price
            profit = max(profit,sell - buy)

        return profit

sol = Solution()
print(sol.maxProfit([10,1,5,6,7,1]))