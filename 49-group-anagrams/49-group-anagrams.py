class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for word in strs:
            sortedWord = tuple(sorted(list(word)))
            anagramMap.setdefault(sortedWord, []).append(word)
        return [x for x in anagramMap.values()]