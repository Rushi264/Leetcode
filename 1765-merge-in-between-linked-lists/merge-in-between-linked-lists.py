class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pt = hd = list1
        for _ in range(a - 1):
            pt = pt.next
        pta = pt.next
        pt.next = list2
        while pt.next:
            pt = pt.next
        for _ in range(b - a):
            pta = pta.next
        pt.next = pta.next
        return hd