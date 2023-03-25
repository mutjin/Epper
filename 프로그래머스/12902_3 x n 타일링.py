def solution(n):
    if n%2!=0:
        return 0
    
    dp=[0]*(n+1)
    dp[2]=3
    
    for i in range(4,n+1,2):
        dp[i]=dp[i-2]*3+sum(dp[:i-2])*2+2
        #새로생긴 모양
        #이전에 특이한 모양 추가
        #특이한 모양 추가
    
    return dp[n]%1000000007