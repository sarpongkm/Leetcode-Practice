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