# Binary Search 

## [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- It's tricky to find the left boundary 
- In this case, use `nums[end_ptr] == target` to make sure the the target could be start at  start_ptr or end_ptr. Otherwise, the start_ptr could skipped the first element 

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        start, end = 0, len(nums)-1
        
        while start + 1 < end:
            mid = (end - start)//2 + start
            
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                    end = mid
            else:
                end = mid

        
        if nums[end] != target and nums[start] !=target:
            return [-1, -1]
        
        if nums[start] == target:
            left = start
        else:
            left = end
        
        
        right = left
        print(left, right)
        while right < len(nums) and nums[right] == target:
            right += 1 
            
        return [left, right-1]


```