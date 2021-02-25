"""
Problem from Page 127 on the "A Practical Guide to Quantitative Finance Interview" 
 
The state: dp[i,j], the maximum expected profit to get when there i red cards and j cards left on the table 

The transition function: dp[i,j] = max(i-j, dp[i-1, j]*(i/(i+j)), dp[i, j-1] * (j/i+j))

Base case: dp[0, j] = j, dp[i, 0] = 0

"""

import numpy as np 

def dynamic_card_game():
    num_red, num_black = 26, 26

    dp = [[0 for j in range(num_black+1)] for i in range(num_red+1)]

    # base case
    for j in range(num_black+1):
        dp[0][j] = j 
    
    for i in range(1,num_red+1):
        for j in range(1, num_black+1):
            dp[i][j] = max(j-i, dp[i-1][j]*(i/(i+j)) + dp[i][j-1]*(j/(i+j)))
    
    # print(np.around(dp,2))
    print_dp(dp)

    return dp[num_red][num_black]

def print_dp(dp):
    for row in dp:
        print(np.around(row,2))

print(dynamic_card_game())

