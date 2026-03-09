# Last updated: 6/2/2026, 12:01:17 PM
import heapq
class Solution(object):
    def maximumScore(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        index1=[]
        for i in range(len(s)):
            if s[i]=='1':
                index1.append(i)
        heap=[]
        p=0
        total=0
        for idx in index1:
            while p<=idx:
                heapq.heappush(heap,-nums[p])
                p+=1
            if heap:
                total+=-heapq.heappop(heap)
            
        return total
                    