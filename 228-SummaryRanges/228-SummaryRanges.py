# Last updated: 6/2/2026, 12:02:49 PM
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans=[]
        if not nums:
            return []
        start=nums[0]
        end=nums[0]
        cur=start+1
        for i in range(1,len(nums)):
            if cur == nums[i]:
                cur+=1
                end=nums[i]
            else:
                if start==end:
                    ans.append(str(start))
                else:
                    ans.append(str(start)+"->"+str(end))
                start=end=nums[i]
                cur=start+1
        if start==end:
            ans.append(str(start))
        else:
            ans.append(str(start)+"->"+str(end))
        return ans