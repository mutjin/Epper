def solution(board, moves):
    answer = 0
    bucket=[]
    for move in moves:
        move-=1
        
        picked=0
        for i in range(len(board)):
            if board[i][move]!=0:
                picked=board[i][move]
                board[i][move]=0

                if bucket and bucket[-1]==picked:
                    bucket.pop()
                    answer+=2
                else:
                    bucket.append(picked)

                break #이거 안해주면 맨 위 값 안나옴

    return answer