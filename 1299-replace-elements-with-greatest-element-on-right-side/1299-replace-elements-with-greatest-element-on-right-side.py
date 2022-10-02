class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #greatestEle = []
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
            #greatestEle.append(max(arr[i+1:]))
        arr[len(arr)-1] = (-1)
        return arr
            