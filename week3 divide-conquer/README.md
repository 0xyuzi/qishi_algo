# Divide and Conquer

- Consider the exit condition
- process the current step
- return by recurive call function with smaller size problem
- proprocess the return from the recursive call
- return the result

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