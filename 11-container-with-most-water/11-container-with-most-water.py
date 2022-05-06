class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        
        l = 0
        r = len(height) - 1
        
        while l <= r:
            width = r-l
            if height[l] < height[r]:
                length = height[l]
            else:
                length = height[r]
            if (length*width) > max:
                max = length * width
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max