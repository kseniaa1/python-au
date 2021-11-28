#Linked list

+ [Reverse Linked List](#reverse-linked-list)
##Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        el_prev = None
        el = head
        while el is not None:
            el_next = el.next
            el.next = el_prev
            el_prev = el
            el = el_next
        return el_prev

```
