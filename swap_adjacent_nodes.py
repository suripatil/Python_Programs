#Q15 - Swap Nodes in Pairs
#Given a linked list, swap every two adjacent nodes and return its head.
#For example,
#Given 1->2->3->4, you should return the list as 2->1->4->3.
#Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

#Ans - 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Iterative Solution
class Solution(object):
        def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head is None or head.next is None):
            return head
            
        curr = head.next
        prev = head
        head = curr
        
        while(True):
            sec = curr.next
            curr.next = prev
            
            if(sec is None or sec.next is None):
                prev.next = sec
                break
            
            prev.next = sec.next
            prev = sec
            curr.next = prev
        return head
     
     #Recursively
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        sec = head.next
        head.next = self.swapPairs(sec.next)
        sec.next = head
        return sec
            

