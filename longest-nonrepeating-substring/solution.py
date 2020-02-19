class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        max_len = 0
        for c in s:
            if c not in substr:
                substr += c
            else:
                i = substr.index(c)
                if len(substr) > max_len:
                    max_len = len(substr)
                substr = substr[i+1:] + c
                
        if len(substr) > max_len:
            max_len = len(substr)
        return max_len


s = "aabaab!bb"
print(Solution().lengthOfLongestSubstring(s))
