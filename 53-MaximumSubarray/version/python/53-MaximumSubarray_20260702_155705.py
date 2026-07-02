# Last updated: 7/2/2026, 3:57:05 PM
1class Solution(object):
2    def productExceptSelf(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        n=len(nums)
8        pref=[1]*n
9        pref[0]=nums[0]
10        suff=[1]*n
11        suff[-1]=nums[-1]
12        for i in range(1,n):
13            pref[i]=pref[i-1]*nums[i]
14        for i in range(n-2,-1,-1):
15            suff[i]=suff[i+1]*nums[i]
16        print(pref)
17        print(suff)
18        nums[0]=suff[1]
19        nums[-1]=pref[-2]
20        for i in range(1,n-1):
21            nums[i]=pref[i-1]*suff[i+1]
22        return nums
23
24        