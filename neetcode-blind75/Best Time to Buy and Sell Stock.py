class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        buy = prices[0]
        sell = prices[0]
        profit = sell - buy

        for i in range(length-1):
            buy = min(buy,prices[i+1])
            sell = prices[i+1]
            profit = max(profit,sell - buy)

        return profit

sol = Solution()
print(sol.maxProfit([10,1,5,6,7,1]))