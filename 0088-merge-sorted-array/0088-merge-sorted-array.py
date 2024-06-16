class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of nums1 and nums2
        # Declare the pointers toward nums1 and nums2
        point_nums1_index = m - 1
        point_nums2_index = n - 1

        # Pointer for the merged version of the List
        pointer_to_merge = m + n - 1

        # Traverse nums1 and nums2 from the back
        while (
            point_nums1_index >= 0 and point_nums2_index >= 0
        ):  # Until merging pointer is over

            # If a value points nums1 is larger
            if nums1[point_nums1_index] > nums2[point_nums2_index]:
                nums1[pointer_to_merge] = nums1[point_nums1_index]
                point_nums1_index -= 1

            # Or same or less than a value points nums2
            else:
                nums1[pointer_to_merge] = nums2[point_nums2_index]
                point_nums2_index -= 1

            # Iterated once
            pointer_to_merge -= 1

        # If there are remaining elements in nums2, copy them over
        while point_nums2_index >= 0:
            nums1[pointer_to_merge] = nums2[point_nums2_index]
            point_nums2_index -= 1
            pointer_to_merge -= 1
