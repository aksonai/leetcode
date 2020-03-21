class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 2 or numRows == 1:
            return s
        
        arr = [''] * numRows
        
        for i, c in enumerate(s):
            rem = i % (2 * numRows - 2)
            if rem in range(numRows, 2 * numRows - 2):
                arr[2 * numRows - 2 - rem] += c
            else:
                arr[rem] += c
                
        return ''.join(arr)
    
    
# Testing the solution  
sol = Solution()
print(sol.convert('PAYPALISHIRING', 4))