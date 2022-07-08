class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagramDic = 26 * [0]
        for i in range(len(s)):
            anagramDic[ord(s[i]) - 97] += 1
            anagramDic[ord(t[i]) - 97] -= 1
        for i in range(len(anagramDic)):
            if anagramDic[i] != 0:
                return False
        return True
            