from itertools import combinations_with_replacement as cwr
from collections import Counter
def solution(n, info):
    max_answer = []
    max_diff=-1
    apeach_case=info[::-1]
    
    for lion_case in cwr(range(11),n):
        lion_case=Counter(lion_case)
        apeach_score,lion_score=0,0
        temp_answer=[0]*11
        for k in range(11):
            temp_answer[k]=lion_case[k]
            if apeach_case[k]==lion_case[k]==0:
                continue
            else:
                if apeach_case[k]>=lion_case[k]:
                    apeach_score+=k
                else:
                    lion_score+=k
        
        temp_diff=lion_score-apeach_score
        if temp_diff>0 and temp_diff>max_diff:
            max_diff=temp_diff
            max_answer=temp_answer
    
    if max_answer:
        return max_answer[::-1]
    else:
        return [-1] 