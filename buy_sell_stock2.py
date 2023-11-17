prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]

class Solution:
    def maxProfit(self, prices):
        i = 0
        total_profit = 0
        while i < len(prices):
            prev = 0 if i == 0 else i - 1
            today_profit = prices[i] - prices[prev]
            if today_profit > 0:
                total_profit += today_profit

            i += 1
        return total_profit

s = Solution()
print(s.maxProfit(prices))