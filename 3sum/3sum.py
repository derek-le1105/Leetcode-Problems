class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0 and [nums[i], nums[j], nums[k]] not in result:
                    result.append([nums[i], nums[j], nums[k]])
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return result