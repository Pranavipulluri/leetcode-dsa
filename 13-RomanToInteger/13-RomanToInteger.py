# Last updated: 6/2/2026, 12:05:24 PM
class Solution(object):
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        n = len(s)
        
        for i in range(n):
            val = roman[s[i]]
            if i + 1 < n and roman[s[i]] < roman[s[i + 1]]:
                total -= val
            else:
                total += val
                
        return total