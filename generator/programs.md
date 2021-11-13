#Programs

+ [String Compression](#string-compression)
+ [Reverse Linked List](#reverse-linked-list)
##String Compression

https://leetcode.com/problems/string-compression/submissions/

```python 
    for i in range(len(stri)):
        data.append(stri[i])
    return data
def check(self, data,index, res):
    a = data[index]
    count = 0
    for i in range(index, len(data)):
        if data[i] == a:
            count +=1
        else:
            break
    if count == 1:
        res.append(a)
    else:
        res.append(a)
        self.delu(res, str(count))
    for i in range(count):
        data.remove(a)
def compress(self, chars: List[str]) -> int:
    res = []
    while len(chars) != 0:
        self.check(chars, 0, res)
    chars.clear()
    chars.extend(res)
    return len(chars)
```
##Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python 
    el_prev = None
    el = head
    while el is not None:
        el_next = el.next
        el.next = el_prev
        el_prev = el
        el = el_next
    return el_prev
```
