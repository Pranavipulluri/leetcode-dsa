# Last updated: 6/2/2026, 12:01:09 PM
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rem0=[]
        rem1=[]
        rem2=[]
        for i in nums:
            if i%3==0:
                rem0.append(i)
            elif i%3==1:
                rem1.append(i)
            else:
                rem2.append(i)
        rem0.sort()
        rem1.sort()
        rem2.sort()
        max_sum=0
        if len(rem0)>=3:
            max_sum=max(max_sum,(rem0[-1]+rem0[-2]+rem0[-3]))
        if len(rem1)>=3:
            max_sum=max(max_sum,(rem1[-1]+rem1[-2]+rem1[-3]))
        if len(rem2)>=3:
            max_sum=max(max_sum,(rem2[-1]+rem2[-2]+rem2[-3]))
        if len(rem0)>=1 and len(rem1)>=1 and len(rem2)>=1:
            max_sum=max(max_sum,(rem0[-1]+rem1[-1]+rem2[-1]))
        return max_sum