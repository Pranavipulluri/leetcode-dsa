# Last updated: 6/2/2026, 12:01:26 PM
class Solution(object):
    def countBalanced(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        def solve(n):
            if n<10:
                return 0
            s=str(n)
            length=len(s)
            memo={}
            def dps(pos,mn,started,difference,l):
                key=(pos,mn,started,difference,l)
                if key in memo:
                    return memo[key]
                if pos==length:
                    return 1 if started and l>=2 and difference==0 else 0
                limit=int(s[pos]) if mn else 9
                res=0
                for d in range(limit+1):
                    nmn=mn and (d==limit)
                    if not started:
                        if d==0:
                            res+=dps(pos+1,nmn,False,difference,l)
                        else:
                            res+=dps(pos+1,nmn,True,d,1)
                    else:
                        if (l+1)%2==1:
                            res+=dps(pos+1,nmn,True,difference+d,l+1)
                        else:
                            res+=dps(pos+1,nmn,True,difference-d,l+1)
                memo[key]=res
                return res
            return dps(0,True,False,0,0)
        return solve(high)-solve(low-1)
            