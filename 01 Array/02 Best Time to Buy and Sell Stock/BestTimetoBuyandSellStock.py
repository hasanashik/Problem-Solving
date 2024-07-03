from typing import List

# Broute force solution


# def maxProfit(prices: List[int]) -> int:
#     max_profit = 0
#     for i in range(len(prices)-1):
#         for j in range(i+1, len(prices)):

#             diff = prices[j]-prices[i]
#             if diff > max_profit:
#                 max_profit = diff
#     return max_profit

def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    if prices:
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)

    return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    max_profit = maxProfit(prices)
    print(max_profit)

    # Time complexity O(len(prices)-1)
    # Space complexity O(len(prices))
