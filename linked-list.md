#Linked list

+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
##Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

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
    def mergeTwoLists(self, list1, list2):
        if list1 is not None and list2 is not None:
         new_list = ListNode(min(list1.val, list2.val))
         if list1.val < list2.val:
             list1 = list1.next
         else:
                list2 = list2.next
        else:
            if list2 is not None:
                new_list = ListNode(list2.val)
                list2 = list2.next
            elif list1 is not None:
                new_list = ListNode(list1.val)
                list1 = list1.next
            else:
                new_list = list1
        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val:
                new_list.append(list1.val)
                list1 = list1.next
            else:
                new_list.append(list2.val)
                list2 = list2.next
        while list1 is not None:
            new_list.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            new_list.append(list2.val)
            list2 = list2.next
        return new_list

```
