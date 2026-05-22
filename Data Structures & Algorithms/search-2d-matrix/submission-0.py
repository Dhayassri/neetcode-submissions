class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr=[]
        for row in matrix:
            for val in row:
                arr.append(val)
        if target in arr:
            return True
        else:
            return False