# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # the intuitive approach is to iterate through both given lists
        # a dummy node can then store the lesser (or equal) of the two values and increment its respective list

        # initialize a dummy node and a tail to reference it; this prevents edge cases of inserting into an empty list
        dummy = ListNode()
        tail = dummy

        # iterate through the two lists until one or both is empty
        while list1 and list2:

            # if the value of list1 is less than the value of list2, save the value of list1 to the tail
            if list1.val < list2.val:
                tail.next = list1

                # increment list1 to the next value
                list1 = list1.next
            
            # otherwise, save the value of list2 to the tail
            else:
                tail.next = list2

                # increment list2 to the next value
                list2 = list2.next
            
            # increment the tail
            tail = tail.next
        
        # check for the remaining portion of list1 if list2 has been iterated through and save the remainder to the tail
        if list1:
            tail.next = list1
        
        # check for the remaining portion of list2 if list1 has been iterated through and save the remainder to the tail
        elif list2:
            tail.next = list2
        
        # if code reaches this point, the dummy node will contain the merged sorted list using the two given lists
        return dummy.next