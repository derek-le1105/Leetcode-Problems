class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
        l = 0
        r = 1
        max = 0
        while r != len(prices):
            diff = prices[r] - prices[l]
            if diff < 1:
                l = r
            else:
                if diff > max:
                    max = diff
            r += 1
        return max
            