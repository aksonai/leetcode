class Solution:
    def twoSum(self, nums, target):
        the_dict = {}
        for i, num_1 in enumerate(nums):
            the_dict[target-num_1] = i
        
        for j, num_2 in enumerate(nums):
            i = the_dict.get(num_2, None)
            if i and i != j:
                return [j,i]          
        return []
            


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
