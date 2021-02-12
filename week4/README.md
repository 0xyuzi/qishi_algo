# Binary Search 
It has two variants
1. Find the K smallest elements problems. In case case, binary search to find a number and count how many elements in the data less or equal to this number
2. Find the minimum number in a sorted array. Search for the index.

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

## [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
- Binary search, O(m+n log(max_num - min_num))
- 一个很重要的条件是要确保找到的kth smallest在matrix中，所以不能找到一个mid就return
- 要不断逼近
- 最后从start开始check是否>=k(因为可能kth num和k+1'th number 是同一个数),如果不行就return end
- [jiuzhang solution](https://www.jiuzhang.com/solution/kth-smallest-element-in-a-sorted-matrix/)


```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return -1 
        
        if len(matrix[0]) == 1:
            return matrix[0][0]
        
        height = len(matrix)
        
        start, end = matrix[0][0], matrix[-1][-1]
        
        while start + 1 < end:
            mid = (end - start)//2 + start
            
            num_less_equal = self.count_less_equal(mid, matrix, height)
            
            if num_less_equal < k:
                start = mid
            else:
                end = mid 
                
        
        if self.count_less_equal(start, matrix, height) >=k:
            return start
        else:
            return end 
        
        
    def count_less_equal(self, mid, matrix, height):
        count = 0
        
        row, col = height - 1, 0
        
        while row >=0 and col < height:
            if matrix[row][col] > mid:
                row -= 1
            else:
                count += row + 1
                col += 1 
        
        return count 
```

## 719. Find K-th Smallest Pair Distance[https://leetcode.com/problems/find-k-th-smallest-pair-distance/]
### First method use binary search (1st version)
- Sort the list at first, then using the method in Leetcode 378. The 2d matrix is constituted row as the list, col as the transport of the list.
- Initialize using 0, and list[-1] - list[0]
- in each search, find the number of difference less or equal to the mid (keep in mind the row will reset to the last row in each col), the count = row - col 
- However, this method get LTE

"""
    4,   62 100
4    x
62   38  x
100  96  38

count += row-col

"""

```python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        if not nums or len(nums) == 1:
            return -1 
        
        nums = sorted(nums)
        
        start, end = 0, nums[-1] - nums[0]
        # print(start, end, nums)
        while start + 1 < end:
            mid = (end - start)//2 + start 
            
            num_less_equal = self.count_less_equal(mid, nums)
            
            if num_less_equal < k:
                start = mid 
            else:
                end = mid 
        
        start_num_less_equal = self.count_less_equal(start, nums)
        
        # print(f"final {start, end, start_num_less_equal, k}")
        
        if start_num_less_equal >= k:
            return start
        else:
            return end
        
    def count_less_equal(self, mid, nums):
    
        count = 0
        diff = 0
        height = len(nums)
        row, col = height-1, 0
        
        for col in range(height):
            row = height - 1 
            while row >=0 and  nums[row] - nums[col] > mid:
                row -=1 
            
            count += row - col
            
        # print(mid, count)
        return count 

```

### Binary search (2nd version)
- The improvement is on the count side
- In the first version, count needs O(n^2) time to finish
- In this version, the count needs O(n) by using two-pointer approach
    - Iterate the right pointer, and maintain the left ptr, count when num[right]-num[left] <= mid, if not just left += 1
    - In next round, since the updated right ptr will be larger than the prev right ptr, the left-ptr is well-maintained 


```python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        if not nums or len(nums) == 1:
            return -1 
        
        nums = sorted(nums)
        
        start, end = 0, nums[-1] - nums[0]
        # print(start, end, nums)
        while start + 1 < end:
            mid = (end - start)//2 + start 
            
            num_less_equal = self.count_less_equal(mid, nums)
            
            if num_less_equal < k:
                start = mid 
            else:
                end = mid 
        
        start_num_less_equal = self.count_less_equal(start, nums)
        
        # print(f"final {start, end, start_num_less_equal, k}")
        
        if start_num_less_equal >= k:
            return start
        else:
            return end
        
    def count_less_equal(self, mid, nums):
    
        count = 0
        left = 0
        for right in range(len(nums)):
             
            while nums[right] - nums[left] > mid:
                left += 1  
            
            count += right - left
            
        # print(mid, count)
        return count 


```

## [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

- Use the `nums[mid]` to compare with `nums[end]`
- if the former less than the later, then shrink the end; otherwise, thrink on the start side
- Finally, compare with the start with end to find the minimum

```python

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None 
        
        start, end = 0, len(nums)-1
        
        
        while start + 1 < end:
            
            mid = (end - start)//2 + start
            # print(nums[start],nums[mid], nums[end])
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid 
                
        # print(nums[start],nums[mid], nums[end])
        
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]


```