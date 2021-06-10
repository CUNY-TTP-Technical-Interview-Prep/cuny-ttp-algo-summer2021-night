# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    curr = head
    prev = None
    while curr:
      nxt = curr.next
      curr.next = prev
      prev = curr
      curr = nxt
    return prev
  
  def reverseList2(self, head: ListNode): # recursive
    def reverse(prev, node):
      if not node: return prev
      nxt = node.next
      node.next = prev
      return reverse(node, nxt)