# Last updated: 6/2/2026, 12:02:04 PM
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A=[]
        B=[]
        for i in range(len(nums)):
            if is_prime(i):
                A.append(nums[i])
            else:
                B.append(nums[i])
        AS=sum(A)
        BS=sum(B)
        return abs(AS-BS)
        