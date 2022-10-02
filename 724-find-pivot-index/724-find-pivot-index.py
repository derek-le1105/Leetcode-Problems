class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = 0
        for num in nums:
            sums += num
        
        LHS, RHS = 0, sums
        for i in range(len(nums)):
            RHS -= nums[i]
            LHS = sums - nums[i] - RHS
            if LHS == RHS:
                return i
        return -1