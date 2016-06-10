#Q - Reverse Linked List - Iterative and Recursive

#Ans - Iterative Method - 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

#Ans - Recursive Solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.service_reverse(head)
        
    def service_reverse(self,node,prev = None):
        if node:
            curr = node
            node = node.next
            curr.next = prev
            prev = curr
            return self.service_reverse(node,prev)    
        return prev

