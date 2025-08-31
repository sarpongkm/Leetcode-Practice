0001. Two Sum
Problem

You’re given an array of integers nums and an integer target. The task is to return the indices of the two numbers that add up to target.

Example

Input:  nums = [2,7,11,15], target = 9  
Output: [0,1]

Solutions
Approach 1: Brute Force

Try out every pair of numbers.

If their sum equals the target, return their indices.

Time Complexity: O(n²)

Space Complexity: O(1)

class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

Approach 2: Hashmap (Efficient)

Use a dictionary to store numbers we’ve seen with their indices.

For each number, check if its complement (target - num) is already in the dictionary.

If yes, return both indices.

Time Complexity: O(n)

Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i

Why Hashmap Wins

Brute force does O(n²) comparisons, which is slow.

Hashmap lookups are O(1) on average, so the whole thing runs in O(n).

Key Takeaways

Learned how brute force vs. optimized approaches compare.

Practiced using a hashmap for constant-time lookups.

Reinforced the idea of starting simple, then improving efficiency.
