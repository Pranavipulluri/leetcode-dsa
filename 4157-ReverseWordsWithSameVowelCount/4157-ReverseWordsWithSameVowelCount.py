# Last updated: 6/2/2026, 12:01:11 PM
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=0
        word=s.split(' ')
        ans=[]
        for c in word[0]:
            if c in 'aeiou':
                count+=1
        ans.append(word[0])
        for i in range(1,len(word)):
            vchar=0
            for c in word[i]:
                if c in 'aeiou':
                    vchar+=1
            if count==vchar:
                ans.append(word[i][::-1])
            else:
                ans.append(word[i])
        return ' '.join(ans)
            