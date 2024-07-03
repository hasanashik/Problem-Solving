# Maximum Profit from Stock Prices

This Python function `maxProfit` calculates the maximum profit that can be obtained from buying and selling a stock given its prices over time.

## Function Description

The function `maxProfit` takes in a list of integers `prices`, where each integer represents the price of a stock on a given day. It returns an integer representing the maximum profit achievable by buying and then selling the stock at the best possible times.

### Script Details

The function works as follows:
- Initialize `max_profit` to 0.
- Initialize `min_price` to the first element of `prices`.
- Iterates through the list starting from the second element.
- For each price in `prices`, update `min_price` if the current price is lower than `min_price`.
- If the current price minus `min_price` is greater than `max_profit`, update `max_profit`.
- Return `max_profit`, which represents the maximum profit possible.

## Example

```python
if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    max_profit = maxProfit(prices)
    print(max_profit)  # Output: 5
	
    # Time complexity O(len(prices)-1)
    # Space complexity O(len(prices))