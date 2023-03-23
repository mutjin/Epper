from collections import deque

n,m,v=map(int,input().split()) #정점개수, 간선개수, 시작정점
graph=[[] for _ in range(n+1)]
visited_bfs=[0]*(n+1)
vistied_dfs=[0]*(n+1)
result_bfs=[]
result_dfs=[]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

def bfs(v):
    queue=deque([v])
    visited_bfs[v]=1
    
    while queue:
        v=queue.popleft()
        result_bfs.append(v)

        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i]=1
    return result_bfs

def dfs(v):
    vistied_dfs[v]=1
    result_dfs.append(v)

    for i in graph[v]:
        if not vistied_dfs[i]:
            dfs(i)
    return result_dfs

print(*dfs(v))
print(*bfs(v))
