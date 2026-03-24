# Last updated: 6/2/2026, 12:01:40 PM
from collections import Counter,defaultdict,deque
class Solution(object):
    def minSwaps(self, nums, forbidden):
        """
        :type nums: List[int]
        :type forbidden: List[int]
        :rtype: int
        """
        n=len(nums)
        c1=Counter(nums)
        c2=Counter(forbidden)
        for x in c1:
            if c1[x]>(n-c2[x]):
                return -1
        badie=[nums[i] for i in range(n) if nums[i]==forbidden[i]]
        if not badie:
            return 0
        k=len(badie)
        freq=Counter(badie)
        mx=max(freq.values())
        return max((k+1)//2,mx)
        if len(badie)==1:
            return 1
        return (badie+1)//2
        b=defaultdict(list)
        for i in badie:
            b[forbidden[i]].append(i)
        """
        for val in nums:
            b[val].append(val)
        target=[0]*n
        j=0
        for i in range(n):
            for val in b:
                if val!=forbidden[i] and b[val]:
                    target[i]=b[val].popleft()
                    break
        
        pos=defaultdict(deque)
        for i,v in enumerate(nums):
            pos[v].append(i)
        """
        flat=[]
        for g in b.values():
            flat.extend(g)
        to={}
        k=len(flat)
        for i in range(k):
            to[flat[i]]=flat[(i+1)%k]
        
        visited=set()
        swaps=0
        for i in flat:
            if i in visited:
                continue
            cycle_len=0
            cur=i
            while cur not in visited:
                visited.add(cur)
                cur=to[cur]
                cycle_len+=1
            swaps+=cycle_len-1
        return swaps