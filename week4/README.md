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

## 287. [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

### Follow up:
- How can we prove that at least one duplicate number must exist in nums?
- Can you solve the problem without modifying the array nums?
- Can you solve the problem using only constant, O(1) extra space?
- Can you solve the problem with runtime complexity less than O(n2)?

### Method
After the constraints above, binary search is the the solution
- Pick a number, count how many elements in the list
- if the number of elements higher than the number, so choose the [start, mid]
- else choose the [mid, end]
- after the loop, check the left and right, count their number and check 

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None 
        
        start, end = 0, len(nums)-1
        
        while start + 1 < end:
            mid = (end - start)//2 + start
            
            num_less = self.count_less_equal(mid, nums)
            # print(mid, num_less)
            if num_less > mid:
                end = mid 
            else:
                start = mid 
        
        
        if self.count_less_equal(start, nums) >start:
            return start
        else:
            return end
        
    def count_less_equal(self, target,nums):
        count = 0
        
        for num in nums:
            if num <= target:
                count += 1 
                
        return count
        


```