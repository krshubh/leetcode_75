class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = prices[0]
        profit = 0
        for i in range(1, len(prices)) :
            temp_profit = prices[i] - min_num
            if (temp_profit > profit):
                profit = temp_profit
            min_num = min(min_num, prices[i])
        return profit