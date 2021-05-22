class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        
        arr = []
        
        for i in range(rowIndex+1):
            arr.append([1]*(i+1))
            
        for r in range(2, rowIndex+1):
            for c in range(1, r):
                arr[r][c] = arr[r-1][c] + arr[r-1][c-1]
        
        return arr[rowIndex]