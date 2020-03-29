class Solution:
    chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0

        sign = 1
        num = 0
        for i,c_1 in enumerate(str):
            if c_1 != ' ':
                str = str[i:]
                break

        if str[0] == '-':
            sign = -1
        elif str[0] == '+':
            pass
        elif str[0] in self.chars:
            num += int(str[0])
        else:
            return 0

        for j,c_2 in enumerate(str[1:]):
            if c_2 in self.chars:
                num = num * 10 + int(c_2)
            else:
                break
        
        num = num * sign
        if num < - 2 ** 31:
            return - 2 ** 31
        elif num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return num



sol = Solution()
print(sol.myAtoi(' 0-91283472332'))

        