class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        a, b = 0, 1
        max_profit = 0

        while b < len(prices):
            if prices[a] > prices[b]:
                a = b
                b += 1
            else:
                max_profit = max(max_profit, prices[b] - prices[a])
                b += 1
        return max_profit