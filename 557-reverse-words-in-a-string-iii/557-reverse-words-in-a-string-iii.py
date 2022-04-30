class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        newS = ""
        for i in range(len(words)):
            chars = list(words[i])
            for j in range(len(chars)/2):
                chars[j], chars[len(chars)-j-1] = chars[len(chars)-j-1],chars[j]
            for x in chars:
                newS += x 
            if i != len(words)-1:
                newS += " "
        return newS