from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        solution = 0

        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                solution += prices[i+1] - prices[i]

        return solution
