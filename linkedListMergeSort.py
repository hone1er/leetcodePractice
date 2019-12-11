# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l2 == None:
            return l1
        if l1 == None:
            return l2
        head = None
        l = l1
        r = l2
        current = None
        while l != None and r != None:
            if l.val <= r.val:
                if current == None:
                    head = l
                    current = l
                    l = l.next
                else:
                    current.next = l
                    current = current.next
                    l = l.next
                    
            else:
                if current == None:
                    head = r
                    current = r
                    r = r.next
                else:
                    current.next = r
                    current = current.next
                    r = r.next
                    
        while l != None:
            current.next = l
            current = current.next
            l = l.next
            
        while r != None:
            current.next = r
            current = current.next
            r = r.next
        return head
    