class Solution:
    def tribonacci(self, n: int) -> int:
        
        arr = [0] * (n+2)
        
        if n == 0:
            return 0
        
        arr[1] = 1
        arr[2] = 1
        
        for i in range(3, n+2):
            arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
        
        return arr[n]