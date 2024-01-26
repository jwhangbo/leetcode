# 15. 3Sum
# https://leetcode.com/problems/3sum/

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # primitive method will be O(n^3) time, which is obviously not desirable
        # the optimized approach will be very similar to problem 167

        # to prevent the issue of having duplicate answers, nums should be sorted
        # the pointers can then skip over duplicate elements to prevent the issue from occurring
        # the same two pointer approach is adjusted to use 3 values for the sum
        # the pointers can be used to sum the leftmost after each iterated value and rightmost numbers in the list
        # i.e. if the list is [-2, -1, 0, 1, 3], then -2 is the iterated value, -1 is the leftmost and 3 is the rightmost
        # if the sum is greater than the target, then the sum should be decreased by decrementing the right pointer
        # if the sum is less than the target, then the sum should be increased by incrementing the left pointer
        # if neither are true, then the pointers sum up to 0 and meet the conditions

        # this method requires both nums to be sorted and two nested loops to find value + two sum
        # therefore, it will run at O(nlogn) + O(n^2), which is simplified to O(n^2)

        # create the list to store all results and sort nums
        res = []
        nums.sort()

        # before continuing, can optimize algorithm by immediately returning an empty list if nums length is less than 3

        # create a while loop to iterate each value in sorted nums
        # use enumerate to also track the pointer of the iterated value
        for i, a in enumerate(nums):

            # check and skip until the iterated value is not a duplicate
            if i > 0 and a == nums[i - 1]:
                continue

            # create the pointers for left and right, where the left is the first value after the iterated value
            l, r = i + 1, len(nums) - 1

            # create a while loop to iterate each value simultaneously from l-r and from r-l
            while l < r:
                
                # get the sum of the 3 values
                threesum = a + nums[l] + nums[r]

                # if the current sum is greater than 0, decrement the right pointer
                if threesum > 0:
                    r -= 1
                
                # if the current sum is less than 0, increment the left pointer
                elif threesum < 0:
                    l += 1

                # if neither is true, the current sum equals 0
                else:
                    
                    # append the indices of the three sum to the results list
                    res.append([a, nums[l], nums[r]])

                    # unlike problem 167, the two pointers do not need to be both decremented and incremented
                    # instead, only the left pointer needs to be incremented
                    # i.e. if the list is [-3, -1, 0, 0, 1, 2, 3], the first solution comes to be [-3, 0, 3]
                    # this means that the left pointer passed -1 to reach the first of the two 0s
                    # the loop below ensures that all duplicate values are skipped

                    # the next check should have the left pointer begin at 1
                    # however, the right pointer does not need to 'reset' back and can start from where it was previously left off
                    # doing this, the right pointer would have to decrement to 2, resulting in finding the second solution [-3, 1 ,2]

                    # afterwards, the left and right pointers will cross, so the next sum to find will move from starting value -3 to -1
                    # the third solution of [-1, 0, 1] will be found after a few decrements on the right pointer
                    
                    # seeing this, there is a possible optimization to stop the for loop when the value is equal or greater than 0
                    # this is due to the fact that nums is now sorted - no sum can be found if the lowest value is already at 0 or greater
                    l += 1
                    
                    # repeat the loop to ensure that the pointer is not a duplicate value
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        # if code reaches this point, all solutions must be appended to the results list
        return res