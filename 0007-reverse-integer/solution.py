class Solution:
    def reverse(self, x: int) -> int:
        if x < - 2 ** 31 or x > 2 ** 31:
            return 0
        elif x < 0:
            str_int = str(x)[1:]
            return - int(str_int[::-1])
        else:
            return int(str(x)[::-1])
        
        
sol = Solution()
print(sol.reverse(-123))