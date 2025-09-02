# 0015. 3Sum

## Problem

Given an integer array `nums`, return all triplets `[nums[i], nums[j], nums[k]]` such that:

* `i != j`, `i != k`, and `j != k`
* `nums[i] + nums[j] + nums[k] == 0`

The solution set **must not contain duplicate triplets**, and the order does not matter.

**Examples**

```
Input:  nums = [-1,0,1,2,-1,-4]  
Output: [[-1,-1,2], [-1,0,1]]  

Input:  nums = [0,1,1]  
Output: []  

Input:  nums = [0,0,0]  
Output: [[0,0,0]]  
```

**Constraints**

* 3 <= nums.length <= 3000
* -10⁵ <= nums\[i] <= 10⁵

## Solutions

### Approach 1: Sort + Two Pointers (Optimal)

* Sort `nums`.
* Fix an index `i` and use two pointers `l` and `r` to find pairs that sum to `-nums[i]`.
* Skip duplicates for `i`, `l`, and `r` to avoid repeated triplets.
* **Time Complexity:** O(n²)
* **Space Complexity:** O(1) (ignoring output)

```python
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate pivot

            l, r = i + 1, n - 1
            target = -nums[i]

            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
```

### Approach 2: Brute Force (Learning Only)

* Try all triplets `(i, j, k)`.
* If they sum to zero, add to a set.
* Very slow, but a good baseline.
* **Time Complexity:** O(n³)
* **Space Complexity:** O(1) (plus dedup set)

```python
class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        seen = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        seen.add((nums[i], nums[j], nums[k]))
        return [list(t) for t in seen]
```

### Why Two Pointers?

* Sorting + two pointers is the cleanest way to hit **O(n²)**.
* Skipping duplicates is straightforward and avoids extra memory.

### Key Takeaways

* 3Sum reduces to repeated **2Sum** searches.
* Sorting helps with both efficiency and duplicate handling.
* It’s critical to think about **deduplication strategy** in these problems.

Would you like me to add **trace tables** (step-by-step values of `i`, `l`, `r`) for one input, like `[-1,0,1,2,-1,-4]`, so your README looks extra interview-ready?
