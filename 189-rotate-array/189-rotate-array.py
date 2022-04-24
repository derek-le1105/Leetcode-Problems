class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        newList = [0] * len(nums)
        
        for i in range(len(nums)):
            newList[(i+k)%len(nums)] = nums[i]
        nums[:] = newList
        
        