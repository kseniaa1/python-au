#Linked list

+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
##Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        end = ListNode(val)
        n = self
        while n.next:
            n = n.next
        n.next = end


class Solution:
    def len(self, node):
        k = 0
        while node:
            k += 1
            node = node.next
        return k

    def getIntersectionNode(self, headA, headB):
        ha = headA
        hb = headB
        len_a = self.len(headA)
        len_b = self.len(headB)
        while len_a > len_b:
            ha = ha.next
            len_a -= 1
        while len_b > len_a:
            hb = hb.next
            len_b -= 1
        while ha:
            if ha == hb:
                return ha
            hb = hb.next
            ha = ha.next
        return None


```
