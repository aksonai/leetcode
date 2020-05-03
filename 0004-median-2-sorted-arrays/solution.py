class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)

        if m == 0:
            mid = len(nums2) // 2
            if n % 2 == 1:
                return nums2[mid]
            else:
                return (nums2[mid-1] + nums2[mid]) / 2

        elif m==1 and n==1:
            return (nums1[0] + nums2[0]) / 2

        total_len = m + n
        min_i = 0
        max_i = m
        
        while min_i <= max_i:
            i = (min_i + max_i) // 2
            j = (total_len + 1) // 2 - i

            if i < m and nums1[i] < nums2[j-1]:
                min_i = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                max_i = i - 1
            else:
                print(i,j)
                break

        if total_len % 2 == 1:
            if i == 0:
                return nums2[j-1]
            elif j == 0:
                return nums1[i-1]
            else:
                return max(nums1[i-1], nums2[j-1])
        else:
            if i == 0:
                if j==n:
                    return (nums2[j-1] + nums1[i]) / 2
                else:
                    return (nums2[j-1] + min(nums2[j], nums1[i])) / 2
            elif j == 0:
                return (max(nums1[i-1], nums2[j]) + nums1[i-1]) / 2
            elif i == m:
                return (max(nums1[i-1], nums2[j-1]) + nums2[j]) / 2
            elif j == n:
                return (max(nums1[i-1], nums2[j-1]) + nums1[i]) / 2
            else:
                return (max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])) / 2
            


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,47,1000,1234,5478,10000,100014]
    nums2 = [2,5,24,5000,6000,6001,7000]
    sorted_nums = sorted(nums1+nums2)
    print(sorted_nums)
    print(sol.findMedianSortedArrays([1], [1]))