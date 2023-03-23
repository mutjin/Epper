from itertools import combinations_with_replacement as cwr
from collections import Counter

def solution(n,info):
    maxdiff=-1
    k=len(info) #점수종류의 개수 (0점~10점으로 11개)
    info.reverse()
    ans=[]

    for case in cwr(range(0,k),n):
        lion_point,apeach_point=0,0
        temp_ans=[0]*k

        case=Counter(case)
        for i in range(k):
            temp_ans[i]=case[i]

            #무효
            if case[i]==info[i]==0:
                continue

            #라이언 승리
            if case[i]>info[i]:
                lion_point+=i
            #어피치 승리
            else:
                apeach_point+=i
        
        if lion_point>apeach_point:
            diff=lion_point-apeach_point
            if diff>maxdiff:
                maxdiff=diff
                ans=temp_ans
        
    if ans:
        return ans[::-1]
    else:
        return [maxdiff]
