    # 광물을 5개의 청크로 분할하고 각 청크에 포함된 종류별 광물의 개수를 센다.
    # 광물의 개수를 기준으로 내림차순으로 정렬한다.

def solution(picks, minerals):
    answer=0
    prd=[[1,1,1],[5,1,1],[25,5,1]]

    for i in range(3):
        picks[i]*=5
        
    i=0
    for mine in minerals:
        if i>3:
            break
        
        if picks[i]>0:
            if mine=="diamond":
                answer+=prd[i][0]
            elif mine=="iron":
                answer+=prd[i][1]
            elif mine=="stone":
                answer+=prd[i][2]
            picks[i]-=1
        else:
            i+=1

    return answer