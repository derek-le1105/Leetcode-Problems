class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxWater = 0
        while l < r:
            minHeight = min(height[l], height[r])
            width = r - l
            currWater = (minHeight*width)
            if maxWater < currWater:
                maxWater = currWater
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
            
        return maxWater