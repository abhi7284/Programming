import sys

def minCoins(amount , coins, dp):

    if amount == 0:
        return 0

    elif dp[amount] != 0 :
        return dp[amount]

    else:
        ans = sys.maxsize
        for i in coins:
            if amount - i >=0:
                subprob = minCoins(amount-i,coins,dp)
                ans = min(ans,subprob)
                
        dp[amount] = ans+1
        return dp[amount]


def minCoinsBU(amount,coins,dp):
    for i in range(2,amount+1):
        dp[i] = sys.maxsize
        for j in coins:
            if amount-j>=0:
                subprob = dp[amount - j]
                dp[i] = min(subprob+1,dp[i]+1)
    return dp[amount]

coins = [1,2,5,10,20,50,100,200]

amount = int(input("Enter amount to be changed: "))
dp = [0]*(amount+1)
dp[0] = 0
dp[1] = 1
print(minCoinsBU(amount,coins,dp))
