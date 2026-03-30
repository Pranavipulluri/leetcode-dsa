# Last updated: 6/2/2026, 12:05:37 PM
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3=nums1+nums2
        nums3.sort()
        n=len(nums3)
        if n%2!=0:
            return nums3[n//2]
        else:
            a=nums3[n/2]
            b=nums3[n/2-1]
            c=(a+b)/2.0
            return c