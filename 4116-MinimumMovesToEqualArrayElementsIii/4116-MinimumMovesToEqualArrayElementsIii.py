# Last updated: 6/2/2026, 12:01:20 PM
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        n=len(nums)
        s=sum(nums)
        return (n*m)-s
        