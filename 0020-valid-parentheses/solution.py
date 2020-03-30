class Solution:
    parens = {'(': ')',
              '[': ']',
              '{': '}'}
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        elif len(s) % 2 == 1 or s[0] in self.parens.values():
            return False

        arr = []
        for paren in s:
            if paren in self.parens.keys():
                arr.append(paren)
            elif self.parens[arr.pop()] != paren:
                return False

        return len(arr) == 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid('{[]}'))