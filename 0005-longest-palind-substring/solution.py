class Solution:
    
    def isPalindrome(substr):
        return substr == substr[::-1]
        
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        longest = s[0]
        s_len = len(s)
        s_copy = s[:]
        for i, c in enumerate(s):
            cut_s = s[i+1:]
            potential_palindrome = c
            while c in cut_s:
                next_i = cut_s.index(c)
                potential_palindrome = potential_palindrome + cut_s[:next_i+1]
                if Solution.isPalindrome(potential_palindrome):
                    if len(potential_palindrome) > len(longest):
                        longest = potential_palindrome
                cut_s = cut_s[next_i+1:]
        return longest
                        
                    
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('aaabaaaa'))          
                
            