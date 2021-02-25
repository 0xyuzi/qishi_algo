# Divide and Conquer

- Consider the exit condition
- process the current step
- return by recurive call function with smaller size problem
- proprocess the return from the recursive call
- return the result
-[快速排序和归并排序的时间复杂度分析——通俗易懂](https://www.cnblogs.com/tuyang1129/p/12857821.html)


## Merge-Sort
- [Python implementation](./merge_sort.py)
- Divide the whole list into two halved size list
- sort each halved list
- then merge two sublists into one by comparing their values

## 105. Construct Binary Tree from Preorder and Inorder Traversal
- [Python implementation](./lc_105_construct_binary_tree_preorder_inorder.py)
- Use the properties of preorder and inorder of binary tree transverse
    - preorder: root at the first location
    - inorder: the left side of the root is left subtree, right side of the root is right substree 

__More efficient implementation using hashmap to store the index of inorder numbers__
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None 
        
        
        in_dict = dict()
        
        for index, num in enumerate(inorder):
            in_dict[num] = index
        
        print(in_dict)
        
        return self.dfs(preorder,inorder, 0, len(preorder)-1,  0, len(inorder)-1, in_dict)
    
    
    def dfs(self, preorder, inorder, pre_start, pre_end, in_start, in_end, in_dict):
        # print(preorder, inorder)
      
        if pre_start > pre_end or in_start > in_end:
            return None 
        
        
        cur_val = preorder[pre_start]
        cur_node = TreeNode(cur_val)
        
        # search for the index of cur_val in inorder
        in_pivot = in_dict[cur_val]
        
        left_size = in_pivot - in_start
        
        
        cur_node.left = self.dfs(preorder, inorder, pre_start+1, pre_start + left_size, in_start, in_pivot-1, in_dict)
        cur_node.right = self.dfs(preorder, inorder, pre_start + left_size+1, pre_end, in_pivot+1, in_end, in_dict)
        
        
        return cur_node
        
    
        



```
## 241. Different Ways to Add Parentheses 
- [Python implementation](./lc_241_diff_ways_add_paren.py)
- Patterns as x opt y, x and y would also like to the sub operations inside 
- minimum element to return is the digits by using `list.isdigit()`

Add the path of module so programs can import from it.
```python
import sys,os
sys.path.append(os.path.realpath('.'))
```

## [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

### priority queue method, k size heap to maintain, time O(nlogk)
    - use dummy node as the head 
    - create new node for the new linked-list

__priority queue sol__
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
    
        dummy = None
        h = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next 

        
        dummy = ListNode(0)
        node = dummy
        
        while h:
            val, index = heappop(h)
            node.next = ListNode(val)
            node = node.next 
            
            if lists[index]:
                heappush(h, (lists[index].val, index))
                lists[index] = lists[index].next
            

        return dummy.next 



```

### divide and conquer
    - divide the lists into two parts
    - two parts do their merge work separately 
    - merge the two parts by using sort 2 linked list method
    - [nice python implementation on leetcode cn](https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/leetcode-23-he-bing-kge-pai-xu-lian-biao-by-powcai/)


__dnq method__
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# divide and conquer
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None 
        
        n = len(lists)
        
        return self.merge_lists(lists, 0, n-1)
        
    def merge_lists(self, lists, left, right):
        if left == right:
            return lists[left]
        
        mid = (right - left)//2 + left
        left_list = self.merge_lists(lists, left, mid)
        right_list = self.merge_lists(lists, mid+1, right)
        
        return self.merge_2_lists(left_list, right_list)
    
    
    def merge_2_lists(self,list1, list2):
        if not list2:
            return list1
        
        if not list1:
            return list2
        
        if list1.val < list2.val:
            list1.next = self.merge_2_lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_2_lists(list1, list2.next)
            return list2 
        

```

## [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- use `partition` function in quick_select method
- select the val mid index as the pivot number (keep in mind use the value not the index since the number at the mid index would probably be swapped) 
- in each partition, find the k in either left part or right part, then recursive call that part with the partition function
- the each partition, the final boundaries would be [....right | mid |left...]



```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k <0:
            return None 
        
        return self.partition(nums, 0, len(nums) - 1, k-1)
        
    def partition(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[k]
            
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
                
        # left is not bigger than right
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        
        return nums[k]


```