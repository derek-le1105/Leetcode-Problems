class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #character must be mapped to one other character ONLY
        #for the example of 'egg' and 'add', 'e' maps to 'a' and 'g' maps to 'd'
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            if(s[i] not in sMap):
                sMap[s[i]] = t[i]
            if(t[i] not in tMap):
                tMap[t[i]] = s[i]
            if(sMap[s[i]] == t[i] and tMap[t[i]] == s[i]):
                continue
            else:
                return False
        return True