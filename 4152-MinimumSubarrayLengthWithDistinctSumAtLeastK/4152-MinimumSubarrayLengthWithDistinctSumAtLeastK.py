# Last updated: 6/2/2026, 12:01:10 PM
class Solution(object):
    def minLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq=defaultdict(int)
        ds=0
        left=0
        ans=float('inf')
        for i in range(len(nums)):
            if freq[nums[i]]==0:
                ds+=nums[i]
            freq[nums[i]]+=1
            while ds>=k:
                ans=min(ans,i-left+1)
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    ds-=nums[left]
                left+=1
        if ans!=float('inf'):
            return ans
        return -1