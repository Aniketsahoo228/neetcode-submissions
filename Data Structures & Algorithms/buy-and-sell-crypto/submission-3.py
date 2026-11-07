class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
Dry Run: prices = [10, 1, 5, 6, 7, 1]

Day | price | Check                            | min_price | max_profit
----|-------|----------------------------------|-----------|-----------
 0  |  10   | 10 < inf  -> Yes, new min        |    10     |     0
 1  |   1   | 1 < 10    -> Yes, new min        |     1     |     0
 2  |   5   | 5 < 1 No, 5 - 1 = 4 > 0  -> Yes  |     1     |     4
 3  |   6   | 6 < 1 No, 6 - 1 = 5 > 4  -> Yes  |     1     |     5
 4  |   7   | 7 < 1 No, 7 - 1 = 6 > 5  -> Yes  |     1     |     6
 5  |   1   | 1 < 1 No, 1 - 1 = 0 > 6  -> No   |     1     |     6

Answer: 6
"""
        
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit