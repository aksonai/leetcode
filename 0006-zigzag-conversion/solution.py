class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = []
        i = 0
        while i < len(s):
            arr.append(s[i:i+numRows])
            for j in range(numRows-2):
                arr.append(s[i+numRows+j])
            i += numRows
           
        print(arr)
        
        
sol = Solution()
sol.convert('PAYPALISHIRING', 4)