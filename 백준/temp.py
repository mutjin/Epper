import sys
from collections import deque
input=sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs():
    queue=deque([[0,0]])
    visited[0,0]=1
    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                if graph[nx][ny]>=1:
                    graph[nx][ny]+=1
                else:
                    visited[nx][ny]=1
                    queue.append([nx,ny])

answer=0
while True:
    visited=[[0 for _ in range(m)] for _ in range(n)]
    bfs()
    flag=0

    for i in range(n):
        for j in range(m):
            if graph[i][j]>=3:
                graph[i][j]=0
                flag=1
            elif graph[i][j]==2:
                graph[i][j]=1
        
        