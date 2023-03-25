n=int(input())
answer=0
times=list(map(int,input().split()))

times.sort()

for i in range(n):
    answer+=times[i]*(n-i)

print(answer)