# Last updated: 6/2/2026, 12:01:22 PM
class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=min(nums)
        b=max(nums)
        missing=[]
        for i in range(a,b):
            if i not in nums:
                missing.append(i)
        return missing