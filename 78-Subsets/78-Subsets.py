# Last updated: 6/2/2026, 12:03:48 PM
from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        for r in range(len(nums)+1):
            result.extend(combinations(nums,r))
        return [list(subset) for subset in result]
        