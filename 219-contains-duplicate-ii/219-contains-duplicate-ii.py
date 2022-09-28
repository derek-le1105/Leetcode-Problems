class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numMap = {}
        for i in range(len(nums)):
            numMap.setdefault(nums[i], []).append(i)
        
        for key in numMap:
            indices = numMap[key]
            if len(indices) <= 1:
                continue
            else:
                for i in range(len(indices)):
                    for j in range(i+1, len(indices)):
                        if abs(indices[i] - indices[j]) <= k:
                            return True
        return False
                