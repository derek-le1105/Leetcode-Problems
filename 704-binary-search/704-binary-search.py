class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        mid = (r-l) // 2
        while l <= r:
            if target == nums[mid]:
                return mid
            if target < nums[mid]:  #if target is less than mid, we take left half of array
                r = mid - 1
                mid = l + (r - l) // 2
            else:
                l = mid + 1
                mid = l + (r - l) // 2
        return -1
                 
        