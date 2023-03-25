line=list(input())
stick=1 #막대기 개수
answer=0

for i in range(1,len(line)):
    if line[i]=="(":
        stick+=1
    else:
        #razer
        if line[i-1]=="(":
            stick-=1
            answer+=stick
        
        #end of stick
        else:
            stick-=1
            answer+=1

print(answer)