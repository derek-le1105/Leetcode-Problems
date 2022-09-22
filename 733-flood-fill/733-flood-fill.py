class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image
        self.fill(image, sr, sc, image[sr][sc], color)
        return image
        
    
    def fill(self, image, sr, sc, prevColor, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        print(sr, sc)
        if image[sr][sc] == color:
            return
        if image[sr][sc] == prevColor:
            image[sr][sc] = color
        else:
            return
        self.fill(image, sr+1, sc, prevColor, color)
        self.fill(image, sr-1, sc, prevColor, color)
        self.fill(image, sr, sc+1, prevColor, color)
        self.fill(image, sr, sc-1, prevColor, color)
        return