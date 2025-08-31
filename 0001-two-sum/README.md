# 0001. Two Sum

## Problem
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

**Example**
Input: nums = [2,7,11,15], target = 9

Output: [0,1]


## Solutions

### Approach 1: Brute Force
- Check every pair of numbers.
- Time Complexity: O(n²)
- Space Complexity: O(1)

```python
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

### Approach 2: Optimized (Hashmap)
Use a dictionary to store numbers and their indices.

For each number, check if target - num has already been seen.

Time Complexity: O(n)

Space Complexity: O(n)

```python
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i

### Why Hashmap?
Brute force → O(n²) comparisons, too slow for large inputs.

Hashmap → O(n) lookups, very efficient.

### Learnings
Learned difference between brute force and optimized solutions.
Understood how hashmaps give constant-time lookup.
Practiced writing both naive and efficient solutions.

