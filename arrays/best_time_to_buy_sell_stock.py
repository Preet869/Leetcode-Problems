# 121. Best Time to Buy and Sell Stocks

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')  # Start with the highest possible value
        profit = 0  # No profit yet

        for price in prices:
            if price < min_price:
                min_price = price  # Found a new lower price to buy
            else:
                profit_today = price - min_price  # Profit if we sell today
                if profit_today > profit:
                    profit = profit_today  # Update max profit if better

        return profit
