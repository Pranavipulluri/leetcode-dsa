# Last updated: 6/2/2026, 12:00:41 PM
class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        for num in nums:
            stack.append(num)
            while len(stack)>=2 and stack[-1]==stack[-2]:
                val=stack.pop()
                stack[-1]=val*2
                
        return stack
            