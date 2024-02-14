# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two approaches - iteratively or recursively
        # for iteratively, a function would loop through each node using two pointers
        # if node exists, the current node would point to the previous node
        # a temporary value must be used to save the current node before being set
        # the iterative approach will be O(n) time complexity and O(1) memory complexity and is the more efficient approach

        # initialize two pointers for the previous and current node in the list of nodes
        # the previous will default to None, while current will default to the head of the given linked list
        prev, curr = None, head

        # loop until curr points to None, at which point the list will have been reversed
        while curr:

            # initialize a temporary holder for the next node for the current node
            nxt = curr.next

            # since curr exists, the next node for the current node must be set to point to the previous node instead
            curr.next = prev

            # the previous node is then set to the current node
            prev = curr

            # finally, the current node is set to the next node saved by the temporary holder, thus iterating through the list
            curr = nxt
        
        # if code reaches this point, prev will contain the reversed linked list
        return prev
    
        # for recursively, the same function can be called until None is found, and setting a new head with each each function call
        # the recursive approach will be O(n) for both time and memory complexity, as it will require the new head to be stored

        # check if the head is set to None and return if true
        # this will be the base condition to stop the recursion
        # if not head:
        #     return None 

        # first set the new head to the current head
        # new_head = head
    
        # check if the head's next node is not None
        # if head.next:
    
        #     call the function again to pass the head's next node and set the return value as the new head
        #     new_head = self.reverseList(head.next)
    
        #     set the head's next next node to be head
        #     head.next.next = head

        # set the head's next value to None
        # head.next = None
    
        # if code reaches this point, new head will contain the reversed linked list
        # return new_head