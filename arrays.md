#Arrays

+ [ Squares of a Sorted Array](#-squares-of-a-sorted-array)
## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/


```python 
   class Solution:
    def first(self,lst):
        k = len(lst)
        for i, numb in enumerate(lst):
            if 0 < int(numb):
                k = i
                break
        return(k)


    def new_list(self, data, num):
        lst1 = []
        lst2 = []
        i = 0
        while i < num:
            lst1.append((-int(data[i]))**2)
            i +=1
        while i < len(data):
            lst2.append(int(data[i])**2)
            i += 1
        lst1.reverse()
        return lst1, lst2


    def sortedSquares(self, num):
        k = self.first(num)
        data1, data2 = self.new_list(num, k)
        i, j = 0, 0
        result = []
        while i < len(data1) and j < len(data2):
            if data1[i] < data2[j]:
                result.append(data1[i])
                i += 1
            else:
                result.append(data2[j])
                j += 1
        result += data1[i:]
        result += data2[j:]
        return result

```
