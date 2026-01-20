# Last updated: 6/2/2026, 12:02:35 PM
class Solution:
    @cache
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        li = []

        for j in range(len(s)):
            count += 1 if s[j] == '1' else -1

            if count == 0:
                mid = self.makeLargestSpecial(s[i + 1:j])
                li.append('1' + mid + '0')
                i = j + 1

        return ''.join(sorted(li, reverse=True))