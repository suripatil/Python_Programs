#Q17. Linked List Cycle
#Given a linked list, determine if it has a cycle in it.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False        
        first = head
        second = first.next
        
        while(second is not None and second.next is not None):
            if(first == second):
                return True
            
	   first = first.next
           second = second.next.next
        return False

