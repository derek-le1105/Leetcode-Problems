# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        while head != None:
            temp = ListNode(head.val)
            temp.next = newHead.next
            newHead.next = temp
            head = head.next
        return newHead.next
        