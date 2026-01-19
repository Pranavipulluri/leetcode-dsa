# Last updated: 6/2/2026, 12:03:43 PM
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target in nums:
            return True
        return False