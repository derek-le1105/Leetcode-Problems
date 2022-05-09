class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)- 1
        while left <= right:
            mid = left + (right-left) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else: #nums[mid] == target
                while left <= right:
                    if nums[left] != target:
                        left += 1
                    elif nums[right] != target:
                        right -= 1
                    if nums[left] == target and nums[right] == target:
                        return [left, right]
                    
                    
                    
            
        return [-1,-1]