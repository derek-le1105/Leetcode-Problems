class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        insertIndex = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex
        