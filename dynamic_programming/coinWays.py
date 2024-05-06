
count = 0

def maxw(n,coins,dp):
    global count
    
    count = count+1

    if n ==0:
        return 1
    
    s = 0
    s2 = 0

    if dp[n]!=0:
        return dp[n]
    
    for i in coins:
        if n-i>=0:
            s = s + maxw(n-i,coins,dp)
            s2 = s2 + maxw(n,coins[1:],dp)
            
    dp[n]=s+s2
            
    return dp[n]

n = int(input("amount: "))
coins = [1,2]
dp = [0]*(n+1)
dp[0]=1
print(maxw(n,coins,dp))
