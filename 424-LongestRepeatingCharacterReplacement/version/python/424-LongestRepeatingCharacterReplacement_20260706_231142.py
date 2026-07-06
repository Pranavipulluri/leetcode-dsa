# Last updated: 7/6/2026, 11:11:42 PM
1class Solution(object):
2    def findMaxAverage(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: float
7        """
8        s=sum(nums[0:k])
9        max_avg=s/float(k)
10        i=0
11        for j in range(k,len(nums)):
12            s+=nums[j]
13            s-=nums[i]
14            i+=1
15            max_avg=max(max_avg,s/float(k))
16        return max_avg
17