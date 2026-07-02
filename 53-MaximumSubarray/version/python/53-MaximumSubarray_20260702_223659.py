# Last updated: 7/2/2026, 10:36:59 PM
1class Solution(object):
2    def twoSum(self, numbers, target):
3        """
4        :type numbers: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        s=0
9        e=len(numbers)-1
10        while s<e:
11            if numbers[s]+numbers[e]<target:
12                s+=1
13            elif numbers[s]+numbers[e]>target:
14                e-=1
15            else:
16                return ([s+1,e+1])
17