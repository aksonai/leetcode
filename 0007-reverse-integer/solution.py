class Solution:
    def reverse_positive(self, x: int) -> int:
        x = abs(x)
        y = 0
        while x:
            quot, rem = divmod(x, 10)
            x = quot
            y = y * 10 + rem
        return y
        
    def reverse(self, x: int) -> int:
        y = self.reverse_positive(x)
        if - y >= - 2 ** 31 and x < 0:
            return - y
        elif y < 2 ** 31 and x >= 0:
            return y
        else:
            return 0
        
        
sol = Solution()
print(sol.reverse(-123))
print(sol.reverse(0))
print(sol.reverse(-2147483648))