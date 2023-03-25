n=int(input())
students=[]
for _ in range(n):
    temp=list(input().split())
    for i in range(1,4):
        temp[i]=int(temp[i])
    students.append(temp)

students.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in students:
    print(i[0])