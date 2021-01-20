# Stock trade problems 

## General template 
- [Summary of stock trade problems in Leetcode discussion](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems)
- [Chinese Translation version](https://leetcode-cn.com/circle/article/qiAgHn/)
```python
dp method
the max profit of trading during first to ith day when allowed trad j times 

1. when current states is not hold stock 
dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + p[i])

2. when current state is hold stock
dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - p[i])

base case:
dp[0][j][0] = 0
dp[0][j][1] = - inf

dp[i][0][0] =  0
dp[i][0][1] = -inf

# specific to this problem
since it no trade time limits, the real limits is the num days //2 (f.i. if days = 6, max trades =3, if day=5, max trade = 2)

# res: dp[N][max_trade]
```
