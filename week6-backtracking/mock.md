# mock backtracking
## [306. Additive Number](https://leetcode.com/problems/additive-number/submissions/)
- [fuminzhuxue solution] (https://blog.csdn.net/fuxuemingzhu/article/details/80661715)
- think about the exit conditions
- think how to deal with the leading zero of more than 1 digit
- think about the stack updated and size of the stack

```python
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        path = []
        return self.dfs(num, 0, path)
    
    def dfs(self, num, start, path):
        # print(num, start, path)
        if len(path) >=3 and path[-1] != path[-2] + path[-3]:
            return False
        
        if start >= len(num) and len(path)>=3:
            return True 
        
        for i in range(start, len(num)):
            cur = num[start:i+1]
            if cur[0] == '0' and len(cur) != 1:
                continue 
            
            if self.dfs(num, i+1, path+[int(cur)]):
                return True
           
        
        return False
        =
```