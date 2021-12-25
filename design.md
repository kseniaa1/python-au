#Design

+ [Min Stack](#min-stack)
## Min Stack

https://leetcode.com/problems/min-stack/

```python 
class MinStack:

    def __init__(self):
        self.b = [];


    def push(self, x: int) -> None:
        self.b.append(x)

    def pop(self) -> int:
        return self.b.pop();

    def top(self) -> int:
        return self.b[-1]

    def getMin(self) -> int:
        c = min(self.b)
        return c

```
