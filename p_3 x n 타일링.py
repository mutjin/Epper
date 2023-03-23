def solution(n):
    if n%2!=0:
        return 0
    
    dp=[0]*(n+1)
    dp[2],dp[4]=3,11
    for i in range(6,n+1,2):
        dp[i]=3*dp[i-2]+2*sum(dp[:i-2])+2
    
    return dp[n]%1000000007