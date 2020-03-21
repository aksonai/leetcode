class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = []
        ss = ''
        for i, c in enumerate(s):
            rem = i % (2 * numRows - 2)
            if rem in range(numRows, 2 * numRows - 2):
                arr.append(c)
            elif rem == numRows - 1:
                ss += c
                arr.append(ss)
                ss = ''
            else:
                ss += c
                
        if ss:
            arr.append(ss)
            
            
        print(arr)
            
        
        # i = 0
        # while i < len(s):
        #     arr.append(s[i:i+numRows])
        #     for j in range(numRows-2):
        #         arr.append(s[i+numRows+j])
        #     i += 2 * numRows - 2
           
        # print(arr)
        
        
sol = Solution()
sol.convert('PAYPALISHIRING', 4)