#Linked list

+ [Sort List](#sort-list)
##Sort List

https://leetcode.com/problems/sort-list/

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


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


class Solution:
    def merge_sort(self, arr):
        if len(arr) < 2:
            return arr[:]
        else:
            middle = int(len(arr) / 2)
            left = self.merge_sort(arr[:middle])
            right = self.merge_sort(arr[middle:])
            return merge(left, right)

    def sortList(self, head):
        a = []
        cur = head
        while cur:
            a.append(cur.val)
            cur = cur.next
        if len(a)!=0:
            a = self.merge_sort(a)
            new = ListNode(a[0])
            for i in range(1, len(a)):
                new.append(a[i])
            return new
        else:
            return head

```
