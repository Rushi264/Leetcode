# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev , curr = None, head
        # we are doin this iteratively. 
        while curr:
            temp = curr.next
            #store our curr.next in temperary variable, before assigning it to prev.
            curr.next = prev
        #None -->  1 --> 2 --> 3 --> 4 --> 5
        #prev   curr   curr.next

        #None <-- 1 -/- 2 --> 3 --> 4 --> 5
        #None   prev   temp  curr.next

        # this process will continue till whole list is inverted.
            prev = curr
            curr = temp
        return prev 