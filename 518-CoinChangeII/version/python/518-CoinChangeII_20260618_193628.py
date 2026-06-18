# Last updated: 6/18/2026, 7:36:28 PM
1class Solution(object):
2    def change(self, amount, coins):
3        """
4        :type amount: int
5        :type coins: List[int]
6        :rtype: int
7        """
8        dp=[0]*(amount+1)
9        dp[0]=1
10        for c in coins:
11            for i in range(c, amount + 1):
12                dp[i] += dp[i - c]
13        return dp[amount]
14        