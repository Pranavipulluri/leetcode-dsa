# Last updated: 6/2/2026, 12:00:53 PM
class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.lower()
        v=0
        cnst=0
        for c in s:
            if c.isalpha():
                if c in 'aeiou':
                    v+=1
                else:
                    cnst+=1
        if cnst>0:
            score=v//cnst
        else:
            score=0
        return score