# python-au

+ [String Compression](#string-compression)

## String Compression

https://leetcode.com/problems/string-compression/


```python
  def delu(self, data, stri):
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
