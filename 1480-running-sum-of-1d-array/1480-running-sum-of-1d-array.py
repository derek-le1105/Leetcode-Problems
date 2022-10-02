class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        
        for i in range(len(nums)):
            if len(runningSum) == 0:
                runningSum.append(nums[i])
                continue
                            
            runningSum.append(nums[i] + runningSum[i-1])
        return runningSum