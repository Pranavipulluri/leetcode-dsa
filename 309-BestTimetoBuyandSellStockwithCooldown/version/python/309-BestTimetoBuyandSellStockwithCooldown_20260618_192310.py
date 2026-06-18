# Last updated: 6/18/2026, 7:23:10 PM
1class Solution(object):
2    def maxProfit(self, prices):
3        """
4        :type prices: List[int]
5        :rtype: int
6        """
7        dp={}
8        def dfs(i,buying):
9            if i>=len(prices):
10                return 0
11            if (i,buying) in dp:
12                return dp[(i,buying)]
13            if buying:
14                buy=dfs(i+1,not buying)-prices[i]
15                cooldown=dfs(i+1, buying)
16                dp[(i,buying)]= max(buy,cooldown)
17            else:
18                sell=dfs(i+2,not buying)+prices[i]
19                cooldown=dfs(i+1, buying)
20                dp[(i,buying)]= max(sell,cooldown)
21            return dp[(i,buying)]
22        return dfs(0,True)
23    
24
25        