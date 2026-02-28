# Last updated: 6/2/2026, 12:01:00 PM
class Solution(object):
    def rotateElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nn=[]
        ans=[]
        if k==0:
            return nums[:]
        for i in range(len(nums)):
            if nums[i]>=0:
                nn.append(nums[i])
        if len(nn)>0 and k:
            j=k%len(nn)
        for i in range(len(nums)):
            if nums[i]>=0:
                ans.append(nn[j])
                j=(j+1)%len(nn)
            else:
                ans.append(nums[i])
        return ans
                