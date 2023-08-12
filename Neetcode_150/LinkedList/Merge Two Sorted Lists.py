# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        current.next = list1 or list2
        return head.next


                 
"""
 # WORNG SOLUTION 

        linkedlist = None
        current1 = list1
        current2 = list2
        while list1.next is not None :
            if current1 >= current2:
                linkedlist = current2
                current2 = list2.next
            else:
                linkedlist = current1
                current1 = list1.next
        return linkedlist
"""
