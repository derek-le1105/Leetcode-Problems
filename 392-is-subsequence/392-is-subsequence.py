class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        
        while l < len(s):
            if r > len(t)-1:
                return False
            if s[l] == t[r]:
                l+=1
            r+=1
        return True