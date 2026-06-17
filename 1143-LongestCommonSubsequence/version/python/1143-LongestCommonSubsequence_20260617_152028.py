# Last updated: 6/17/2026, 3:20:28 PM
# 2d dp, diagnolly checking
1class Solution(object):
2    def longestCommonSubsequence(self, text1, text2):
3        """
4        :type text1: str
5        :type text2: str
6        :rtype: int
7        """
8        dp=[[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
9        for i in range(len(text1)-1,-1,-1):
10            for j in range(len(text2)-1,-1,-1):
11                if text1[i]==text2[j]:
12                    dp[i][j]=1+dp[i+1][j+1]
13                else:
14                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
15        return dp[0][0]
16        