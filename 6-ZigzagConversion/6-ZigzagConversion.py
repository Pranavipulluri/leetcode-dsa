# Last updated: 6/2/2026, 12:05:34 PM
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows>=len(s):
            return s
        rows=["" for _ in range(min(numRows,len(s)))]
        cur=0
        goingdown=False
        for c in s:
            rows[cur]+=c
            if cur==0 or cur==numRows-1:
                goingdown=not goingdown
            cur+=1 if goingdown else -1
        return "".join(rows)
