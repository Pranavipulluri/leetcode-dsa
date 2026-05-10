# Last updated: 6/2/2026, 12:03:02 PM
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        prev=[]
        ans=[]
        for i in range(1,numRows+1):
            if i==1:
                ans.append([1])
                prev.append(1)
            else:
                curr=[]
                curr.append(1)
                if len(prev)>1:
                    for j in range(1,len(prev)):
                        curr.append(prev[j-1]+prev[j])
                curr.append(1)
                prev=curr
                ans.append(curr)
        return ans

        