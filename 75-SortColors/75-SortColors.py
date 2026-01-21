# Last updated: 6/2/2026, 12:03:52 PM
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count0=0
        count1=0
        count2=0
        for i in nums:
            if i==0:
                count0+=1
            elif i==1:
                count1+=1
            else:
                count2+=1
        nums[:]= [0]*count0 + [1]*count1 + [2]*count2
        

