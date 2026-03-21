# Last updated: 6/2/2026, 12:01:36 PM
from collections import defaultdict,Counter
class Solution(object):
    def interactionCosts(self, n, edges, group):
        """
        :type n: int
        :type edges: List[List[int]]
        :type group: List[int]
        :rtype: int
        """
        total=Counter(group)
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ans=[0]
        def dfs(u,parent):
            cnt=Counter()
            cnt[group[u]]=1
            for v in adj[u]:
                if v==parent:
                    continue
                child=dfs(v,u)
                for g in child:
                    ans[0]+=child[g]*(total[g]-child[g])
                if len(child)>len(cnt):
                    cnt,child=child,cnt
                for g in child:
                    cnt[g]+=child[g]
            return cnt
        dfs(0,-1)
        return ans[0]