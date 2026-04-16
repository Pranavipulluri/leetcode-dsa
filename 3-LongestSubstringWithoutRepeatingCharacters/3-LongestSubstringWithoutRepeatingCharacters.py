# Last updated: 6/2/2026, 12:05:38 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s1=""
        l=0
        if(len(s)==1):
            return 1
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] in s1:
                    if l<len(s1):
                        l=len(s1)
                    s1=""
                    break
                else:
                    s1+=s[j]
        return l
