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
        for i in range(count/2):
            head = head.next
        return head
        
        #since we don't know what the length of the linked list is, we have two pointers where both are pointing to first node
        #we traverse the linked list with the first pointer to see how long the linked list is
        #after finding out the length, use the second pointer to get the middle of the linked list using the length