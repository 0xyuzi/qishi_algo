# Leetcode problem on DP

## [53. Maximum Subarray](https://leetcode-cn.com/problems/maximum-subarray/)
- Define the DP, in this problem, the 1-D dp[i] means the max sum subarray ends in index i

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        if len(nums) == 1:
            return nums[0]
        
        length = len(nums)
        
        dp = [0]*(length)
        dp[0] = nums[0]
        
        
        for i in range(1, length):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            
        
        
        return max(dp)

```

## [152 Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- What's the different between this with max subarray sum? (deal with max number)
- so in addition to dp array, what additional variables needed for this (store the min, max prod so far)
- [solution explain](https://leetcode-cn.com/problems/maximum-product-subarray/solution/dpfang-fa-xiang-jie-by-yang-cong-12/)

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        length = len(nums)
        
        dp = [0]*length
        
        dp[0] = nums[0]
        max_dp, min_dp = nums[0], nums[0]
        
      
        for i in range(1, length):
            temp_max = max_dp
            max_dp = max(max_dp*nums[i], min_dp*nums[i], nums[i])
            min_dp = min( temp_max*nums[i], min_dp*nums[i], nums[i])
            dp[i] = max_dp
            
        # print(dp)
        
        return max(dp)

```

## [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- From which direction to think about the dp? (backward should be easier)
- think the base cases
- think about the reward of deletion operation is zero
- [solution explain](https://leetcode-cn.com/problems/longest-common-subsequence/solution/dong-tai-gui-hua-zhi-zui-chang-gong-gong-zi-xu-lie/)


```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
        
        len_txt1, len_txt2 = len(text1), len(text2)
        
        dp = [[0]*(len_txt2+1) for _ in range(len_txt1+1)]
        
        for i in range(1, len_txt1+1):
            for j in range(1, len_txt2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        
        return dp[len_txt1][len_txt2]
```

[516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
- think about the meaning of dp[i,j]
- transit function in ways of dp[i+1, j-1], dp[i, j-1], dp[i+1, j], with their rewards 
- base case of dp[i,i], what does it means?
- The computation direction in terms of i and j 

![plot](./figs/labuladong-516.jpg)

__direction code__

```python
# one way of direction
for diag in (1, N):
    for i in range(N-diag):
        j = i + diag

# another way of direction (in C++) by Labuladong
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i + 1; j < n; j++) {
            // 状态转移方程
            if (s[i] == s[j])
                dp[i][j] = dp[i + 1][j - 1] + 2;
            else
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
        }
    }

```
__code__
```python

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        
        height = len(s)
        dp = [[0]*height for _ in range(height)]
        
        for i in range(height):
            dp[i][i] = 1 
        
        for diag in range(1, height):
            for i in range(height - diag):
                j = diag + i
                
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i+1][j-1]+2, dp[i+1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][height-1]
```