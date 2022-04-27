# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 1
        tempHead = head.next
        while tempHead != None:
            count += 1
            tempHead = tempHead.next
        for i in range(count//2):
            head = head.next
        return head
        