class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set(nums)
        if len(hashset) < len(nums):
            return True
        else:
            return False