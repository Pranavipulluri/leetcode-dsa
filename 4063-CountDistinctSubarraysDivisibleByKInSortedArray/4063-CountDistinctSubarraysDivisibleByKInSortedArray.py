# Last updated: 6/2/2026, 12:01:39 PM
from collections import Counter
import fractions
class Solution(object):
    def numGoodSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        n=len(nums)
        if n==0:
            return 0
        prefix_mod=[0]*(n+1)
        curr=0
        for i,x in enumerate(nums):
            curr+=x
            prefix_mod[i+1]=curr%k
        freq=Counter(prefix_mod)
        total_index_pairs=0
        
        for f in freq.values():
            total_index_pairs+=f*(f-1)//2
        subtract_pairs=0
        add_distinct=0
        i=0
        while i<n:
            j=i
            while j+1<n and nums[j+1]==nums[i]:
                j+=1
            m=j-i+1
            v=nums[i]
            block_counter=Counter(prefix_mod[i:j+2])
            block_pairs=0
            for f in block_counter.values():
                block_pairs+=f*(f-1)//2
            subtract_pairs+=block_pairs
            g=fractions.gcd(v%k,k)
            if g==0:
                distinct_l=m
            else:
                L0=k//g
                distinct_l=m//L0
            add_distinct+=distinct_l
            i=j+1
        result=total_index_pairs-subtract_pairs+add_distinct
        return result