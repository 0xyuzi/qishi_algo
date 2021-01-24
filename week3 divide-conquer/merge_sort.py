"""
Merge sort
"divide-conquer"
separete the problem in smaller problems to solve
1. first split the list into half sublists
2. sort each halved list 
3. merge them back 
"""

class Solution:

    def merge_sort(self, nums):
        """
        input: list
        output: list
        """
        print(f"nums: {nums}")
        if len(nums) <= 1:
            return nums 
        
        
        len_nums = len(nums)
        mid = len_nums//2 

        l_list, r_list = nums[:mid], nums[mid:]

        # solve in half list
        l_list = self.merge_sort(l_list)
        r_list = self.merge_sort(r_list)

        print(f"after merge two sub lists, get {l_list, r_list}")

        # merge to together 
        res = []

        l,r = 0, 0
        print(f"after sort l_list, r_list {l_list, r_list}")

        while l < len(l_list) or r < len(r_list):
            
            
            if l == len(l_list):
                res.append(r_list[r])
                r+= 1 
                continue
            
            if r == len(r_list):
                res.append(l_list[l])
                l += 1 
                continue 

            if l_list[l]<r_list[r]:
                res.append(l_list[l])
                l += 1
                 
            else:
                res.append(r_list[r])
                r += 1
            
            print(l,r)
        print(f"after merge get {res}")
        return res 


nums = [12, 11, 13, 5, 6, 7]
sol = Solution()
sol.merge_sort(nums)
