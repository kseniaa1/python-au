#Linked list

+ [Palindrome Linked List](#palindrome-linked-list)
##Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getHalf(selfself, head):
        half = head
        double_half = head
        while double_half is not None and double_half.next is not None:
            half = half.next
            double_half = double_half.next.next
        return half

    def reverseList(self, head):
        el_prev = None
        el = head
        while el is not None:
            el_next = el.next
            el.next = el_prev
            el_prev = el
            el = el_next
        return el_prev

    def isPalindrome(self, head):
        rev = self.reverseList(self.getHalf(head))
        cur = head
        while rev is not None:
            if rev.val == cur.val:
                cur = cur.next
                rev = rev.next
            else:
                return False
        return True

```
