# Last updated: 6/2/2026, 12:02:22 PM
class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        b_count = 0  # number of 'b's seen so far
        res = 0      # minimum deletions
        
        for char in s:
            if char == 'b':
                b_count += 1
            elif char == 'a':
                # Either delete this 'a' or delete all previous 'b's
                res = min(res + 1, b_count)
                
        return res
        