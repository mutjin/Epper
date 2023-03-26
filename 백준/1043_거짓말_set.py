# set과 union, intersection 연산을 이용해서 풀었다
import sys
input=sys.stdin.readline

n,m=map(int,input().split()) #사람수, 파티수
truths=set(input().split()[1:])
parties=[]
answer=0

for _ in range(m):
    parties.append(set(input().split()[1:]))

# set1&set2
# set1.intersection(set2)

# setl|set2
# set1.union(set2)
for _ in range(m):
    for party in parties:
        if truths&party: #파티 참여자 중 진실 아는 사람 있으면
            #union 연산 후 갱신 필요하다
            truths=truths.union(party) #모든 파티 참여자들은 진실을 알게 된다

for party in parties:
    if party&truths:
        continue
    else:
        answer+=1

print(answer)