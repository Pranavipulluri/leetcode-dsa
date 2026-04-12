# Last updated: 6/2/2026, 12:02:16 PM
class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=nums[0]
        numss=nums[-1:0:-1]
        numss.sort()
        ans+=numss[1]+numss[0]
        return ans