n=int(input())
plst=list(map(int,input().split()))

plst.sort()
ans=0
for i in range(n):
    ans+=plst[i]*(n-i)

print(ans)