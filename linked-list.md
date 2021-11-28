#Programs

+ [Middle of the Linked List](#middle-of-the-linked-list)
##Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        cur = head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        el = head
        for i in range(count//2):
            el = el.next
        return el

```
