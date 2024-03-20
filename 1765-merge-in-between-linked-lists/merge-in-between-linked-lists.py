# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        # Create a dummy node to handle cases where the removal starts from the head of list1
        dummy = ListNode(0)
        dummy.next = list1
        
        # Traverse to the (a-1)th node
        current = dummy
        for i in range(a):
            current = current.next
        
        # Save the reference to the (a-1)th node
        before_a = current
        
        # Traverse to the bth node
        for i in range(a, b + 1):
            current = current.next
        
        # Save the reference to the (b+1)th node
        after_b = current.next
        
        # Connect the (a-1)th node to list2
        before_a.next = list2
        
        # Traverse to the end of list2
        while list2.next:
            list2 = list2.next
        
        # Connect the end of list2 to the (b+1)th node
        list2.next = after_b
        
        return dummy.next

