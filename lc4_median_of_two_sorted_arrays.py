# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # the given constraint prevent the usage of merging the two given lists, due to the time complexity expectation of O(log(m+n))
        # instead, the approach should take advantage of the fact that the two given lists are already sorted
        # by definition, a median would be the "middle" value of the combined list if the length is odd
        # if the length is even, the median would be the average of the two "middle" values
        # in other words, a median can be instead interpreted as the halfway point of the merged list

        # conceptually, this can be emulated by taking partitions of the list to avoid merging them
        # the approach would begin by calculating the default values of the partition by referencing the smaller of the two lists
        # the partitions would then be checked for validity and adjusted as needed

        # initialize A and B as nums1 and nums2 by default
        A, B = nums1, nums2

        # initialize the total length of the two lists and the halfway point, rounded down
        total = len(nums1) + len(nums2)
        half = total // 2

        # check if A is smaller than B and swap if not; this is to maintain the idea of A being the smaller list of the two
        if len(A) > len(B):
            A, B = B, A
        
        # itialize two pointers for the leftmost and rightmost values in A
        l, r = 0, len(A) - 1

        # loop until one of the two conditions for finding the median are met, as it is guaranteed
        while True:

            # calculate the middle value of A
            i = (l + r) // 2

            # calculate the middle value of B; the subtraction of 2 is necessary to convert the value to an index
            j = half - i - 2

            # calculate the values for the left and right partitions for A to compare in order to find if a median has been found
            # default to infinity or negative infinity if i or j are found to be out of bounds
            A_left = A[i] if i >= 0 else float("-infinity")
            A_right = A[i + 1] if (i + 1) < len(A) else float("infinity")

            # calculate the values for the left and right partitions for B to compare in order to find if a median has been found
            # default to infinity or negative infinity if i or j are found to be out of bounds
            B_left = B[j] if j >= 0 else float("-infinity")
            B_right = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # check if both the left and right partitions are correct
            if A_left <= B_right and B_left <= A_right:

                # if the length is odd, calculate the median
                if total % 2:
                    return min(A_right, B_right)
                
                # if the length is even, take the average to calculate the median
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            # reduce the size of the left partition
            elif A_left > B_right:
                r = i - 1

            # increase the size of the left partition
            else:
                l = i + 1