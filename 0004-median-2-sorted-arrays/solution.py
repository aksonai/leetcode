class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            i, j = self.find_i_j(nums1, nums2, total_len + 1)
            if i == 0 or j == 0:
                return (nums1[i] + nums2[j]) / 2
            else:
                return max(nums1[i], nums2[j])
        else:
            i, j = self.find_i_j(nums1, nums2, total_len)
            if i == 0 or j == 0:
                return (nums1[i] + nums2[j]) / 2
            else:
                return (max(nums1[i], nums2[j]) + min(nums1[i+1], nums2[j+1])) / 2 
    
    def find_i_j(self, nums1, nums2, total_len):
        min_i = 0
        max_i = len(nums1)
        
        while min_i <= max_i:
            i = (min_i + max_i) // 2
            j = total_len // 2 - i

            if i < len(nums1) and nums1[i] < nums2[j-1]:
                min_i = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                max_i = i - 1
            elif i == 0:
                j -= 1
                break
            elif j == 0:
                i -= 1
                break
            else:
                break

        return i, j


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,47,1000,1234,5478,10000,10001]
    nums2 = [2,5,24,5000,6000,6001,7000]
    # 1,2,5,24,47,1000,1234,5000,5478,6000,10000,10001
    print(sol.findMedianSortedArrays([3],[1,2]))