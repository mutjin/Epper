def solution(board, moves):
    answer = 0
    size=len(board[0])
    bucket=[]
    
    for move in moves:
        j=move-1
        for i in range(size):
            if board[i][j]!=0:
                if bucket and bucket[-1]==board[i][j]:
                    bucket.pop()
                    answer+=2
                else:
                    bucket.append(board[i][j])
                board[i][j]=0
                break
    
    return answer