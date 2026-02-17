# Last updated: 6/2/2026, 12:00:46 PM
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        n,m=len(nums1),len(nums2)
        dp=[[[-10**18]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                dp[i][j][0]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                for p in range(1,k+1):
                    dp[i][j][p]=max(
                        dp[i-1][j][p],dp[i][j-1][p],dp[i-1][j-1][p-1]+nums1[i-1]*nums2[j-1]
                    )
        return dp[n][m][k]