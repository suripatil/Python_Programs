#Q11 - Remove Duplicates from Sorted List

#Given a sorted linked list, delete all duplicates such that each element appear only once.
#For example,
#Given 1->1->2, return 1->2.
#Given 1->1->2->3->3, return 1->2->3.

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None):
            return head
            
        first = head   
        sec = head.next
        while(sec is not None):
            if(first.val < sec.val):
                first.next = sec
                first = sec
            #Handle Duplicates at last
            if(first.val <= sec.val and sec.next is None):
                first.next = sec.next
            sec = sec.next
        return head

