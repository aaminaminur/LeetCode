class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = len(nums1) - 1
        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[idx] = nums1[m-1]
                m-=1
            else:
                nums1[idx] = nums2[n-1]
                n-=1
            idx-=1
        while m:
            nums1[idx] = nums1[m-1]
            m-=1
            idx-=1
        while n:
            nums1[idx] = nums2[n-1]
            n-=1
            idx-=1
        