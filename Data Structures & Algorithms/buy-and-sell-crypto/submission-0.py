class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 101
        profit = 0
        for R in range(len(prices)):
            if prices[R] < L:
                L = prices[R]
            if L < prices[R]:
                profit = max(profit, prices[R] - L)
        return profit