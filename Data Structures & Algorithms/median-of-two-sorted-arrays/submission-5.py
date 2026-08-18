class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        left = 0
        right = len(nums1)
        while left <= right:
            i = (left + right)//2
            j = (len(nums1) + len(nums2) + 1)//2 - i

            nums1_left = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right = float('inf') if i == len(nums1) else nums1[i]
            nums2_left = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right = float('inf') if j == len(nums2) else nums2[j]

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    median = (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    median = max(nums1_left, nums2_left)
                return median
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1