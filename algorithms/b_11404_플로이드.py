n=int(input())
m=int(input())

INF=100001
graph=[[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=min(graph[a][b],c)

#플로이드-워셜 알고리즘
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                graph[i][j]=0
            else:
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

#출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print(0,end=" ")
        else:
            print(graph[i][j],end=" ")
    print()