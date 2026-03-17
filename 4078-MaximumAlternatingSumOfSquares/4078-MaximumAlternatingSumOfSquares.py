# Last updated: 6/2/2026, 12:01:30 PM
from collections import Counter
class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1=[]
        n2=[]
        nums=[x**2 for x in nums]
        nums.sort()
        n=len(nums)
        for i in range(n//2):
            n1.append(nums[i])
        for j in range(n//2,n):
            n2.append(nums[j])
        a=sum(n1)
        b=sum(n2)
        return b-a