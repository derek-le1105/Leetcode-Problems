class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        tripletSum = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sums = nums[l] + nums[r] + nums[i]
                if sums > 0:
                    r-=1
                elif sums < 0:
                    l+=1
                else:
                    tripletFound = [nums[i], nums[l], nums[r]]
                    if tripletFound not in tripletSum:
                        tripletSum.append(tripletFound)
                    l+=1
        return tripletSum