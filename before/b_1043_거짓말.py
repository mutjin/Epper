n,m=map(int,input().split()) #사람수, 파티수
tlst=list(map(int,input().split()))[1:] #진실아는사람수, 진실아는사람번호들
answer=0

for _ in range(m):
    plst=list(map(int,input().split()))[1:]

    for i in tlst:
        if i in plst:
            answer+=1
            break
    
print(answer)
            
