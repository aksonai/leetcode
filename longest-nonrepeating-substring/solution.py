class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        substr_dict = {}
        for c in s:
            print('c: ', c)
            if c not in substr:
                substr += c
                print('substr: ', substr)
            else:
                i = substr.index(c)
                substr_dict[substr] = len(substr)
                substr = substr[i+1:] + c
                
        substr_dict[substr] = len(substr)
        return max(substr_dict.values())


s = "aabaab!bb"
print(Solution().lengthOfLongestSubstring(s))
