import sys

def maxProfit(wines,dp,year,i,j):

    if i>j:
        return 0

    if dp[i][j]!=0:
        return dp[i][j]

    
    else:
        opt1 = wines[i]*year + maxProfit(wines,dp,year+1,i+1,j)
        opt2 = wines[j]*year + maxProfit(wines,dp,year+1,i,j-1)

        dp[i][j] = max(opt1,opt2)

    return max(opt1,opt2)



wines = [2,3,5,1,4]
lw=len(wines)
dp = [[0]*lw]*lw

print(maxProfit(wines,dp,1,0,len(wines)-1))
