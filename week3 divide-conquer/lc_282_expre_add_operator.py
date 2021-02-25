import sys,os
sys.path.append(os.path.realpath('./'))
from typing import List
from helper_func import print_stack


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(num, target, pos, exp, prev, curr, ans):
            if pos == len(num):
                if curr == target:
                    ans.append(exp)
                return 
            for l in range(1, len(num)-pos+1):
                t = num[pos:pos+l]
                if t[0] == "0" and len(t) > 1: break
                n = int(t)
                print(n, pos,l)
                if pos == 0:
                    dfs(num, target, l, t, n, n, ans)
                    continue 
                # print(f"operation + in")
                # print_stack()
                # dfs(num, target, pos+l, exp+'+'+t, n, curr+n, ans)
                # print_stack()
                # print(f"operation + out")
                # print(f"operation - in")
                # print_stack()
                # dfs(num, target, pos+l, exp+'-'+t, -n, curr-n, ans)
                # print_stack()
                # print(f"operation - out")
                # print_stack()
                # print(f"operation * in")
                # print_stack()
                # dfs(num, target, pos+l, exp+'*'+t, prev*n, curr-prev + prev*n, ans) 
                # print(f"operation * out")
                # print_stack()
                
        ans = []
        dfs(num, target, 0, "", 0, 0, ans)
        return ans


nums = "123"
target = 6
sol = Solution()
print(sol.addOperators(nums,target))