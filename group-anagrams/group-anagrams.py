class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramMap = dict()
        for word in strs:
            temp = tuple(sorted(list(word)))
            if temp not in anagramMap:
                anagramMap[temp] = [word]
            else:
                anagramMap[temp].append(word)
        return anagramMap.values()