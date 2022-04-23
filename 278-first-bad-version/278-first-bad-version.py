# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        firstDetected = float('inf')
        left = 0
        right = n
        while left <= right:
            middle = left + (right - left) / 2
            if isBadVersion(middle):
                if middle < firstDetected:
                    firstDetected = middle
                else:
                    right = middle - 1
            else:
                left = middle + 1
        return firstDetected