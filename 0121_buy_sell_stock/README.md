# 0121. Best Time to Buy and Sell Stock

## Problem

You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.
Choose **one** day to buy and a later day to sell to maximize profit.
Return the maximum profit; if no profit is possible, return `0`.

**Examples**

```
Input:  prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy at 1 (day 1) and sell at 6 (day 4), profit = 5.

Input:  prices = [7,6,4,3,1]
Output: 0
Explanation: No profitable transaction; return 0.
```

**Constraints**

* 1 <= prices.length <= 10^5
* 0 <= prices\[i] <= 10^4



## Solutions

### Approach 1: Brute Force (Check All Pairs)

* Try every `(buy, sell)` pair with `buy < sell`.
* Track the best profit seen.

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        best = 0
        for i in range(n):
            for j in range(i + 1, n):
                best = max(best, prices[j] - prices[i])
        return best
```


### Approach 2: One-Pass (Track Min Price So Far) — Optimal

* Keep the **minimum price seen so far**.
* At each day, compute profit if sold today: `prices[i] - min_price`.
* Update the answer and `min_price` as you scan.

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        best = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                best = max(best, p - min_price)
        return best
```



### Approach 3: Kadane’s on Daily Deltas (Nice Alternative)

* Convert to daily differences: `diff[i] = prices[i] - prices[i-1]`.
* Now we want the **maximum subarray sum** over `diff`, but negatives reset to 0.
* The result equals the best single buy-sell profit.

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        current = 0
        best = 0
        for i in range(1, len(prices)):
            current = max(0, current + (prices[i] - prices[i - 1]))
            best = max(best, current)
        return best
```


### Why the One-Pass Method?

* Brute force is simple but too slow for `10^5` elements (O(n²)).
* One-pass maintains just two numbers (`min_price`, `best`) and finishes in O(n), perfect for large inputs.
* Kadane’s is conceptually elegant and also O(n), but the one-pass min-tracker is the most direct.


### What Did I Learn?

* How to turn a naive O(n²) search into an O(n) scan using running minima.
* The link between “buy low, sell high” and **maximum subarray** (Kadane’s algorithm).
* Edge cases: strictly decreasing arrays should return `0`; arrays of length 1 also return `0`.


### Quick Step-by-Step (One-Pass) on `[7,1,5,3,6,4]`

* `min=∞ → 7 → 1`
* Day 1 (price 7): min=7, best=0
* Day 2 (price 1): min=1, best=0
* Day 3 (price 5): profit=4, best=4
* Day 4 (price 3): profit=2, best=4
* Day 5 (price 6): profit=5, best=5
* Day 6 (price 4): profit=3, best=5
  Return `5`.
