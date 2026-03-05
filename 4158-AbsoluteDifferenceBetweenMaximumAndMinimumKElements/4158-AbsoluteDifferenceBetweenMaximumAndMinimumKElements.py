# Last updated: 6/2/2026, 12:01:07 PM
class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        max_k=sum(nums[-k:])
        min_k=sum(nums[:k])
        return(max_k-min_k)