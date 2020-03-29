class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        reversed_num = 0
        while num:
            quot, rem = divmod(num, 10)
            reversed_num = reversed_num * 10 + rem
            num = quot
        return reversed_num == x


sol = Solution()
print(sol.isPalindrome(121))