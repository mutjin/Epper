t=int(input())
answer=t #모두 그룹 단어라고 가정

for _ in range(t):
    word=input()
    letters=[word[0]] #첫번째 단어는 미리 처리
    
    #글자가 바뀐 경우
    for i in range(1,len(word)):
        if word[i-1]!=word[i]: #글자가 바뀐 경우에 대해서만 판단
            if word[i] in letters:
                answer-=1 #그룹 단어가 아니므로 빼기
                break #아닌거 확인했으면 더 볼 필요 없잖아
            else:
                letters.append(word[i])

print(answer)