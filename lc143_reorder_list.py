# 143. Reorder List
# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # similiar to problem 21, the list can be split into two partitions and consecutively iterated through
        # the halfway point can be found by using a fast and slow pointer
        # the slow pointer will increment by 1 and the fast pointer will increment by 2
        # this ensures that for both odd and even length lists, the slow pointer + 1 will point to the start of the second partition
        # to make the approach easier, the second parition will be reversed

        # this approach will run at O(n) time complexity and O(1) memory complexity

        # initialize two pointers for the fast and slow pointers
        slow, fast = head, head.next

        # increment until the fast pointer hits the end of the list
        while fast and fast.next:

            # the slow pointer will increment by 1 and the fast pointer will increment by 2
            slow = slow.next
            fast = fast.next.next

        # initialize a pointer for the start of the second partition
        second = slow.next

        # initialize two placeholder pointers to track the previous value
        prev = slow.next = None

        # iterate until the second partition reaches the end
        while second:

            # temporarily store the next value
            tmp = second.next

            # change the pointer for the next value to the previous value, thus reversing the list
            second.next = prev

            # set the previous value to be the current value
            prev = second

            # set the current value to the next value stored in tmp
            second = tmp
        
        # initialize two lists to act as the two partitions
        first, second = head, prev

        # iterate until the second partition reaches the end
        while second:

            # temporarily store the next value for the first and second partitions
            tmp1, tmp2 = first.next, second.next

            # change the pointer for the next value in the first partition to the current value of the second partition
            first.next = second

            # change the pointer for the next value in the second partition to the next value of the first partition
            second.next = tmp1

            # set the current values of the first and second partitions to the values stored in tmp
            first, second = tmp1, tmp2