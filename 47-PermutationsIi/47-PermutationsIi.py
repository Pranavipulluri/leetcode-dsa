# Last updated: 6/2/2026, 12:04:34 PM
from itertools import permutations
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(set(permutations(nums)))
        