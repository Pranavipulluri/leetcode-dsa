# Last updated: 6/2/2026, 12:01:55 PM
from collections import Counter
class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n=len(nums)
        if n%k!=0:
            return False
        total_groups=n//k
        freq=Counter(nums)
        for num,count in freq.items():
            if count>total_groups:
                return False
        return True
        