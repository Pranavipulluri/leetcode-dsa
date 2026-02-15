# Last updated: 6/2/2026, 12:00:43 PM
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi=deque()
        mini=deque()
        l=0
        ans=0
        for r in range(len(nums)):
            while maxi and nums[maxi[-1]]<=nums[r]:
                maxi.pop()
            maxi.append(r)
            while mini and nums[mini[-1]]>=nums[r]:
                mini.pop()
            mini.append(r)
            while (nums[maxi[0]]-nums[mini[0]])*(r-l+1)>k:
                l+=1
                if maxi and maxi[0]<l:
                    maxi.popleft()
                if mini and mini[0]<l:
                    mini.popleft()
            ans+=(r-l+1)
        return ans