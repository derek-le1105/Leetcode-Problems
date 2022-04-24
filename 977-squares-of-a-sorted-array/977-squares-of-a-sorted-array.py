class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftPtr = 0
        rightPtr = len(nums) - 1
        newList = [0] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[leftPtr]) < abs(nums[rightPtr]):
                newList[i] = nums[rightPtr] ** 2
                rightPtr -= 1
            else:
                newList[i] = nums[leftPtr] ** 2
                leftPtr += 1
        return newList