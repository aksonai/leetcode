class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        min_i = 0
        max_i = len(nums1)
        
        while True:
            i = (min_i + max_i) // 2
            j = (len(nums1) + len(nums2) + 1) // 2 - i
            
            if nums1[i-1] <= nums2[j] and nums2[j-1] <= nums1[i]:
                break
            elif nums1[i-1] > nums2[j]:
                min_i = i + 1
            else:
                max_i = i - 1

        return i, j


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,47,1000,1234,5478,10000,10001,200000]
    nums2 = [2,5,24,5000,6000,6001]
    # 1,2,5,24,47,1000,1234,5000,5478,6000,10000,10001
    print(sol.findMedianSortedArrays(nums1,nums2))