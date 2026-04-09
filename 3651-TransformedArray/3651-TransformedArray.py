# Last updated: 6/2/2026, 12:02:11 PM
class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                res.append(nums[i])
            else:
                j=(i+nums[i])%n
                res.append(nums[j])
        return res