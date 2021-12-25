#Design

+ [Implement Stack using Queues](#implement-stack-using-queues)
## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python 
class MyStack:

    def __init__(self):
        self.b = [];


    def push(self, x: int) -> None:
       self.b.append(x)

    def pop(self) -> int:
       return self.b.pop();

    def top(self) -> int:
        return self.b[-1]

    def empty(self) -> bool:
        return not self.b

```
