

def maxw(n,jump,dp):

    if n ==0:
        return 1
    
    s = 0

    if dp[n]!=0:
        return dp[n]
    
    for i in range(1,jump+1):
        if n-i>=0:
            s = s + maxw(n-i,jump,dp)
    dp[n]=s
            
    return dp[n]

n = int(input("total steps: "))

jump = int(input("max jump: "))

dp = [0]*(n+1)

print(maxw(n,jump,dp))
