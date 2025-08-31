# 0121. Best Time to Buy and Sell Stock

## Problem

You’re given an array `prices` where `prices[i]` is the stock price on day `i`.
Pick **one day to buy** and a later day to sell to maximize profit.
If no profit is possible, return `0`.

**Examples**

```
Input:  prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy at 1, sell at 6 → profit = 5.  

Input:  prices = [7,6,4,3,1]
Output: 0
Explanation: No profitable transaction.
```


## Solutions

### Approach 1: Brute Force

* Check all `(buy, sell)` pairs.
* Track the maximum profit.
* **Time Complexity:** O(n²)
* **Space Complexity:** O(1)

```python
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        best = 0
        for i in range(n):
            for j in range(i + 1, n):
                best = max(best, prices[j] - prices[i])
        return best
```


### Approach 2: One-Pass (Track Minimum Price) ✅

* Track the minimum price seen so far.
* At each step, compute profit if we sold today.
* Update the best profit along the way.
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

```python
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        best = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                best = max(best, p - min_price)
        return best
```


### Approach 3: Kadane’s Algorithm on Differences

* Turn stock prices into daily differences: `diff[i] = prices[i] - prices[i-1]`.
* Now it’s a **maximum subarray problem** (Kadane’s).
* Result = maximum sum of consecutive positive deltas.
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

```python
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        current = 0
        best = 0
        for i in range(1, len(prices)):
            current = max(0, current + (prices[i] - prices[i - 1]))
            best = max(best, current)
        return best
```


### Why One-Pass Is the Go-To

* Brute force is way too slow for `10^5` inputs.
* One-pass only needs to remember two numbers (`min_price`, `best`), making it clean and optimal.
* Kadane’s is elegant but overkill compared to one-pass.


### Key Takeaways

* Learned how to reduce an O(n²) approach to O(n).
* Saw the connection between stock trading and Kadane’s max subarray.
* Important edge cases: strictly decreasing prices → return `0`; single-day arrays → return `0`.
