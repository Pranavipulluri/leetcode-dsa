# Last updated: 6/2/2026, 12:04:19 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:                
        end = len(s) - 1

        while s[end] == " ":
            end -= 1
        
        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        
        return end - start