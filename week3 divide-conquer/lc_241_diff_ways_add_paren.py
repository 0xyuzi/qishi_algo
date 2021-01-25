import inspect
from typing import List, Set, Dict, Tuple, Optional

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # parse the string for nums and operators
        if input.isdigit():
            print(f"the input is digit as {input}")
            print_frames(inspect.stack())
            return [int(input)]
        
        res = []
        
        for i, val in enumerate(input):
            if val in ["+", "-", "*"]:
                print(f"into left recursive")
                print_frames(inspect.stack())
                left = self.diffWaysToCompute(input[:i])
                print(f"finish left recursive, into right recursive")
                print_frames(inspect.stack())
                right = self.diffWaysToCompute(input[i+1:])
                print("finish right recursive call")
                print_frames(inspect.stack())
                print(f"into combination of left, right {left, right}")
                for l in left:
                    for r in right:
                        if val == "+":
                            res.append(l+r)
                            continue
                        if val == "-":
                            res.append(l-r)
                            continue
                        if val=="*":
                            res.append(l*r)
                print(f"res: {res}")
        return res 

# print the stack of recursive call
def print_frames(frame_list):
    module_frame_index = [i for i,f in enumerate(frame_list) if f.function == '<module>'][0]
    for i in range(module_frame_index):
        d = frame_list[i][0].f_locals
        local_vars = {x: d[x] for x in d}

        print( "[Frame {} '{}': {}]".format(module_frame_index - i, frame_list[i].function, local_vars))
    print("[Frame '<module>']\n")


# test the function
input = "2-1-1"

sol = Solution()
print(sol.diffWaysToCompute(input))