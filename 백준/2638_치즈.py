import sys
input=sys.stdin.readline

from collections import deque

answer=0
n,m=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]


graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs():
    queue=deque([[0,0]]) #queue=deque([0,0])
    visited[0][0]=1

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            #공기를 기준으로 탐색한다
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                #주변이 치즈인 경우 접촉시간 증가시켜준다
                if graph[nx][ny]>=1:
                    graph[nx][ny]+=1
                #주변이 공기인 경우 탐색 대상 큐에 추가한다
                else:
                    visited[nx][ny]=1
                    queue.append([nx,ny])

while True:
    visited=[[0 for _ in range(m)] for _ in range(n)]
    bfs()
    flag=0

    for i in range(n):
        for j in range(m):

            #치즈가 녹아 없어진다
            if graph[i][j]>=3:
                graph[i][j]=0
                flag=1
            
            #공기가 두 면만 닿은 치즈는 원래 치즈 값인 1로 돌려준다
            if graph[i][j]==2:
                graph[i][j]=1
    
    # 녹은 치즈가 있다면
    if flag==1:
        answer+=1
    # 녹은 치즈가 없다면
    else:
        break

print(answer)