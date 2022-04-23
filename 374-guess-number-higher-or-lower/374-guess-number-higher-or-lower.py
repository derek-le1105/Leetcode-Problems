# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:
            middle = l + (r-l)/2
            if guess(middle) == -1:
                r = middle - 1
            elif guess(middle) == 1:
                l = middle + 1
            else:
                return middle
                
        