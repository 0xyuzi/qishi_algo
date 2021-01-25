import inspect
from typing import List, Set, Dict, Tuple, Optional
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool: 
        if not nums:
            return False 
        
        target, mod = divmod(sum(nums), k)
        
        print(target, mod)
        
        if mod != 0:
            return False
       
        visited = set()
        # (start, cum_sum, numbers, target, k, visited)
        return self.dfs(0, 0, nums, k, target, visited)
    
    def dfs(self, start, cum_sum, nums, k, target, visited):
        
        if cum_sum == target:
            print("dfs call when cum_sum == target")
            print_frames(inspect.stack())
            return self.dfs(0, 0, nums, k-1, target, visited)
        
        if k == 1:
            return True
        
        for i in range(start, len(nums)):
            if i in visited:
                continue 
            
            if cum_sum + nums[i] <= target:
                visited.add(i)
                print("dfs called in the loop")
                print_frames(inspect.stack())
                if self.dfs(i+1, cum_sum + nums[i], nums, k, target, visited):
                    print("dfs return loop if true")
                    return True
                visited.remove(i)
                print("dfs return loop if false")
                print_frames(inspect.stack())
                
        return False 


def print_frames(frame_list):
    module_frame_index = [i for i,f in enumerate(frame_list) if f.function == '<module>'][0]
    for i in range(module_frame_index):
        d = frame_list[i][0].f_locals
        local_vars = {x: d[x] for x in d}

        print( "[Frame {} '{}': {}]".format(module_frame_index - i, frame_list[i].function, local_vars))
    print("[Frame '<module>']\n")



if __name__ == "__main__":
    sol = Solution()
    nums = [4,3,2,3,5,2,1]
    k = 4

    print(sol.canPartitionKSubsets(nums, k))
