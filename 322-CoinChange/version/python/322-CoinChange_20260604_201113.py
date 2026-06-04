# Last updated: 6/4/2026, 8:11:13 PM
# 1D dp
1class Solution(object):
2    def coinChange(self, coins, amount):
3        """
4        :type coins: List[int]
5        :type amount: int
6        :rtype: int
7        """
8        dp=[amount+1]*(amount+1)
9        dp[0]=0
10        for i in range(amount+1):
11            for j in coins:
12                if i-j>=0:
13                    dp[i]=min(dp[i],1+dp[i-j])
14        return dp[amount] if dp[amount]!=amount+1 else -1