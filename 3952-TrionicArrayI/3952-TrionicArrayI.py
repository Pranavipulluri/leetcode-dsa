# Last updated: 6/2/2026, 12:02:00 PM
class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        if n < 4:
            return False

        i = 0

        # increasing
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
        if i == 0 or i == n - 1:
            return False

        # decreasing
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1
        if i == n - 1:
            return False

        # increasing
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1

        return i == n - 1
