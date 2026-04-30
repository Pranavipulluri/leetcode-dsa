# Last updated: 6/2/2026, 12:02:56 PM
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n=len(s)
        res=[]
        feq={}
        for i in range(n-9):
            sub = s[i:i+10]
            feq[sub] = feq.get(sub, 0) + 1

            if feq[sub] == 2:
                res.append(sub)
        return res


        