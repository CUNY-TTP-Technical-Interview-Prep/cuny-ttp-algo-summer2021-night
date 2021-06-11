// Prompt https://leetcode.com/problems/linked-list-cycle/


// Solution:
const hasCycle = function(head) {
  // initialize two pointers at the head node
  let slow = head
  let fast = head
  // if fast pointer or its next or its next next becomes null, return false
  while (fast && fast.next && fast.next.next) {
    // slow pointer moves one steps at a time
    slow = slow.next;
    // fast pointer moves two steps at a time
    fast = fast.next.next;
    // if they meet, return true
    if (slow === fast) {
      return true;
    }
  }
    return false;
};
