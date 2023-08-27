"""
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to
sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def max_profit(prices: list[int]) -> int:
    buy, sell, profit = prices[0], 0, 0
    for price in prices:
        if buy > price:
            buy, sell = price, 0
        elif sell < price:
            sell = price
            if sell - buy > profit:
                profit = sell - buy
    return profit


if '__main__' == __name__:
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    print('All tests passed!')
