#Design

+ [Implement Queue using Stacks](#implement-queue-using-stacks)
## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python 
class MyQueue:

    def __init__(self):
        self.b = [];
        self.e = [];
    def push(self, x: int) -> None:
        while self.e:
            self.b.append(self.e.pop())
        self.e.append(x)
        while self.b:
            self.e.append(self.b.pop())
    def pop(self) -> int:
        return self.e.pop()
    def peek(self) -> int:
        return self.e[-1]
    def empty(self) -> bool:
        return not self.e

```
