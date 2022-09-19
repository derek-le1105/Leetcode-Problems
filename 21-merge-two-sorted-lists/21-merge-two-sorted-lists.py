# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedHead = ListNode()
        merged = mergedHead
        while list1 != None or list2 != None:
            if list1 == None:
                merged.next = ListNode(list2.val, ListNode())
                list2 = list2.next
                merged = merged.next
                continue
            elif list2 == None:
                merged.next = ListNode(list1.val, ListNode())
                list1 = list1.next
                merged = merged.next
                continue
            
            if list1.val > list2.val:
                merged.next = ListNode(list2.val, ListNode())
                merged = merged.next
                list2 = list2.next
            else:
                merged.next = ListNode(list1.val, ListNode())
                merged = merged.next
                list1 = list1.next
        merged.next = None
        return mergedHead.next
                