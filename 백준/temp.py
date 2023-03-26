def dfs(queen,size,row):
    count=0

    if size==row:
        return 1
    
    for col in range(size):
        queen[row]=col

        for x in range(row):
            if queen[x]==queen[row]:
                break

            if abs(queen[x]-queen[row])==row-x:
                break

        else:
            count+=dfs(queen,size,row+1)
    
    return count

def solution(n):
    queen=[0]*n
    return dfs(queen,n,0)