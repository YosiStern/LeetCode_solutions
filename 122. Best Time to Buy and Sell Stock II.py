"""
122. Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""


def max_profit(prices) -> int:
    buy, sell, profit = prices[0], prices[0], 0
    for price in prices:
        if buy > price:
            buy = sell = price
        else:  # sell < price:
            sell = price
        if sell > buy:
            profit += sell - buy
            sell = buy = price
    return profit


if '__main__' == __name__:
    assert max_profit([7, 1, 5, 3, 6, 4]) == 7
    assert max_profit([1, 2, 3, 4, 5]) == 4
    assert max_profit([7, 6, 4, 3, 1]) == 0
    print('All tests passed!')
