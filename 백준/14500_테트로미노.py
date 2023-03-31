import sys
input=sys.stdin.readline

#열 행 선택할수있는블럭수 현재까지더한값
def dfs(row,col,idx,total):
    global answer
    if answer>=total+max_val*(3-idx):
        return
    if idx==3:
        answer=max(answer,total)
        return
    else:
        for i in range(4):
            nrow=row+drow[i]
            ncol=col+dcol[i]

            if 0<=nrow<n and 0<=ncol<m and visited[nrow][ncol]==0:
                # idx가 1일 때 (두 개의 블럭을 선택했을 때) 새로운 블럭에서 다음 블럭을 탐색하는 것이 아니라 다시 기존블럭에서 탐색하게 만들면 ㅗ 모양을 만들 수 있다
                if idx==1:
                    visited[nrow][ncol]=1
                    dfs(row,col,idx+1,total+graph[nrow][ncol])
                    visited[nrow][ncol]=0
                visited[nrow][ncol]=1
                dfs(nrow,ncol,idx+1,total+graph[nrow][ncol])
                visited[nrow][ncol]=0



n,m=map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]

dcol=[0,-1,0,1]
drow=[-1,0,1,0]
answer=0
max_val=max(map(max,graph))

for row in range(n):
    for col in range(m):
        visited[row][col]=1
        dfs(row,col,0,graph[row][col])
        visited[row][col]=0

print(answer)