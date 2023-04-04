class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeroPlaces = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroPlaces.append([i, j])
        
        for places in zeroPlaces:
            self.zeroRow(places[0], matrix)
            self.zeroCol(places[1], matrix)
    
    def zeroRow(self, i,  matrix):
        #change j for row
        for row in range(len(matrix[0])):
            matrix[i][row] = 0
        
        
    def zeroCol(self, j, matrix):
        #change i for col
        for col in range(len(matrix)):
            matrix[col][j] = 0