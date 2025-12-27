# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        #we are creating a dummy node for handling the edge case.
        tail = dummy
        #in order to iterate through our res List, we are storing dummy in tail.

        while list1 and list2:
            #if both list are non null we move forward.
            if list1.val < list2.val:
                #if list1 value is greater than list2 we will add our list val in the res list.
                tail.next = list1
                list1 = list1.next
                #we will update our curr list1 to list1.next
            else:
                #we are doing same if list2 is greater.
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            #if either one of the list is empty we want to append the other list to our result .
            #so we are doing this for for both list1 and list2, eighter one of them might have some 
            #nodes remaining at the end of merging.
            tail.next = list1
        elif list2:
            tail.next = list2
        #we will return our dummy.next which will be the start of our new List.
        return dummy.next

        