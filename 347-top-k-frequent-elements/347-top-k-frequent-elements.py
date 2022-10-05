class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kList = []
        intDict = {}
        highestNum = 0
        for num in nums:
            if num in intDict:
                intDict[num] += 1
            else:
                intDict[num] = 1
        intDict = sorted(intDict.items(), key=lambda item: item[1])
        kList = [x[0] for x in intDict]
        return kList[len(kList)-k:]