class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit=0
        bestbuy=prices[0]
        for i in range(len(prices)):
            if prices[i] < bestbuy:
                bestbuy=prices[i]
            else:
                maxProfit=max(maxProfit, prices[i] - bestbuy)

        return maxProfit   