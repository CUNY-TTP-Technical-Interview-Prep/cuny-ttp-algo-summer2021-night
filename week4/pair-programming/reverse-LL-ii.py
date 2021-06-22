#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        find the linked list from m to n. reverse it.
        pointers to keep track of the reversed m node & reversed n node.
        so that I could point m.next to the original n + 1. 
        point start.next to reversed m. 
        
        1) move pointer start to the node right before m
        2) initialize two pointers, prev, curr to help reverse linked list m -> n. at the end of reversal, curr will be 5. prev will be 4.
        3) point start.next.next to curr
        4) point start.next to prev
        '''
        if m == n: return head
        start = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m-1):
            start = start.next
        prev = None
        curr = start.next # taking the place of node m
        for _ in range(n-m+1):
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        start.next.next = curr
        start.next = prev
        return dummy.next
# @lc code=end

