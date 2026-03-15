# Last updated: 6/2/2026, 12:04:43 PM
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        if 1 not in s:
            return 1
        m=max(nums)
        n=len(nums)
        for i in range(1,n+1):
            if i not in s:
                return i
        return m+1