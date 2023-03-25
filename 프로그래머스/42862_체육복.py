def solution(n, lost, reserve):
    answer = 0
    clothes=[-1]+[1]*(n)+[-1]
    for i in lost:
        clothes[i]-=1
    for i in reserve:
        clothes[i]+=1
    
    for i in range(1,n+1):
        if clothes[i]==0:
            if clothes[i-1]>1:
                clothes[i-1]-=1
                clothes[i]+=1
            else:
                if clothes[i+1]>1:
                    clothes[i+1]-=1
                    clothes[i]+=1
    
    for i in range(1,n+1):
        if clothes[i]!=0:
            answer+=1
    
    print(clothes)
    return answer