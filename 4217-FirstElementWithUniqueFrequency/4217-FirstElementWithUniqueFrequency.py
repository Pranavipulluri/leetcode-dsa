# Last updated: 6/2/2026, 12:00:37 PM
class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        counts={}
        for key,val in freq.items():
            if val not in counts:
                counts[val]=1
            else:
                counts[val]+=1
        for n in nums:
            if counts[freq[n]]==1:
                return n
        return -1