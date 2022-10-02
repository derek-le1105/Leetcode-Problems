class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestEle = []
        for i in range(len(arr)-1):
            temp = arr[i+1:]
            greatestEle.append(max(arr[i+1:]))
        greatestEle.append(-1)
        return greatestEle
            