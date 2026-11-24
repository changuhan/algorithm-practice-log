# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        init = ListNode()
        tail = init 

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Cut the list into two halves
        second = slow.next
        slow.next = None

        # Step 3: Reverse the second half
        prev = None
        while second:
            nxt = second.next     # save the next node
            second.next = prev    # point backward
            prev = second         # move prev forward
            second = nxt          # move second forward
        second = prev             # new head of reversed half

        # Step 4: Merge alternately
        first = head
        while second:
            tmp1 = first.next     # save both next nodes
            tmp2 = second.next

            first.next = second   # first → second
            second.next = tmp1    # second → old first.next

            first = tmp1          # move both forward
            second = tmp2


        

