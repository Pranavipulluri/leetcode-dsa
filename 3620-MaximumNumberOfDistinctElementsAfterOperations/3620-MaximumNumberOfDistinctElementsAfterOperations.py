# Last updated: 6/2/2026, 12:02:13 PM
class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        last=-10**20
        count=0
        for num in nums:
            start=num-k
            end=num+k
            pos=max(start,last+1)
            if pos<=end:
                count+=1
                last=pos
        return count