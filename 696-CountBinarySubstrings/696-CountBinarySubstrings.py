# Last updated: 6/2/2026, 12:02:37 PM
class Solution(object):
    def countBinarySubstrings(self, s):
        prev_group = 0
        curr_group = 1
        ans = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_group += 1
            else:
                ans += min(prev_group, curr_group)
                prev_group = curr_group
                curr_group = 1
        
        ans += min(prev_group, curr_group)
        return ans
