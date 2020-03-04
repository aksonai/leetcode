class Solution:
    
    def isPalindrome(substr):
        return substr == substr[::-1]
        
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        longest = s[0]
        s_len = len(s)
        for i, c in enumerate(s):
            if c in s[i+1:]:
                next_i = s_len - s[::-1].index(c) - 1
                potential_palindrome = s[i:next_i+1]
                if Solution.isPalindrome(potential_palindrome):
                    if len(potential_palindrome) > len(longest):
                        longest = potential_palindrome
        return longest
                        
                    
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('aaabaaaa'))          
                
            