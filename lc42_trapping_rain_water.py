# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # first, the algorithm for what constitutes rain water being trapped must be found
        # by definition, rain water can only be trapped if there are bars surrounding the left and right side of a target bar
        # the height of the target bar must also be less than the minimum of the left and right heights
        # i.e. for an list [1, 0, 1], the middle bar can contain 1 unit of water based on the algorithm
        # even if this array had a greater height on one side, like [5, 0 ,1], the middle bar can still only hold 1 unit of water

        # knowing this, the primitive method is to store the max left and right heights for each bar/height on two different lists
        # to do this, the height list can be iterated both l-r and r-l to track the maximum height for each side
        # afterwards, a third list can take the minimum of the max left and right heights for each bar/height
        # finally, a fourth list would subtract the height of each bar with the minimum of the max left and right heights
        # note that all negative values resulting from this subtraction would be equivalent to 0 units of water stored

        # the primitive method will be O(n) time complexity but also use O(n) memory
        # this method can be simplified to use O(n) time complexity with O(1) memory
        # to achieve this, two pointers will be used

        # similar to problem 11, the two pointers will take the leftmost and rightmost heights
        # since no water can be stored at each end, it is safely assumed that the total units of water at this point will be 0
        # if the left height is greater than the right height, decrement the right pointer and check if any units of water can be stored
        # this is done by using the algorithm described above
        # the key is that the "true" max heights of each side do not need to be known in order to calculate if water can be trapped
        # by tracking the max height of the left and right side and incrementing/decrementing accordingly, this value alone is sufficient
        # for instance, in a list [2, 0, 100, 0, 1], the optimized method will see that the left height is greater
        # therefore, the right pointer will be decremented, where the height is 0 and the minimum left/right height is 1
        # this guarantees that at this position, only one unit of water will be stored
        # even if there is a bar of height 100 next to it, the algorithm will only care about the minimum of the two sides
        # on the flip side, if the height 100 was swapped to height 0, the minimum is still at 1, resulting in the same answer
        # while it may not be intuitive, the algorithm will never require the exact heights of each bar to calculate the water trapped

        # check the edge case of empty list first
        if not height:
            return 0

        # create the pointers for left and right
        l, r = 0, len(height) - 1

        # initialize two numbers to track the left and right maximum heights
        lmax, rmax = height[l], height[r]

        # initialize a number to track the sum of all trapped units of water found so far
        res = 0

        # create a while loop to iterate each height
        while l < r:

            # if the left max height is less than the right max height, increment the left pointer to possibly find a greater height
            if lmax < rmax:
                l += 1

                # compare against the existing max left height and save the larger of the two
                lmax = max(lmax, height[l])

                # add the units of water found at this height
                # note that the primitive method's case of negative values for units of water cannot logically occur here
                # this is due to the fact that the above statement ensures that lmax is at worst equal to the height, resulting in 0
                res += lmax - height[l]
            
            # repeat the same logic for when the right max height is less than or equal to the left max height
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
            
         # if code reaches this point, the sum of all units of water stored in the list of heights will have been found
        return res