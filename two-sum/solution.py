class Solution:
    def twoSum(self, nums, target):
        complement_dict = {}
        for i, num in enumerate(nums):
            if num in complement_dict:
                return [complement_dict[num], i]
            else:
                complement_dict[target - num] = i
        return []
            

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
