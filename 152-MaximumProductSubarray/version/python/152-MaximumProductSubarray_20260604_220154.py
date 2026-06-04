# Last updated: 6/4/2026, 10:01:54 PM
# 1d dp with 2 variables
1class Solution(object):
2    def maxProduct(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        res=max(nums)
8        mins,maxs=1,1
9        for n in nums:
10            if n==0:
11                mins,maxs=1,1
12            else:
13                temp=maxs*n
14                maxs=max(maxs*n,mins*n,n)
15                mins=min(temp,mins*n,n)
16                res=max(res,maxs)
17        return res