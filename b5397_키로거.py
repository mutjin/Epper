t=int(input())

for _ in range(t):
    words=input()
    lefts,rights=[],[]
    
    for word in words:
        if word=="<":
            if lefts:
                rights.append(lefts.pop())
        elif word==">":
            if rights:
                lefts.append(rights.pop())
        elif word=="-":
            if lefts:
                lefts.pop()
        else:
            lefts.append(word)
    
    lefts.extend(reversed(rights))
    print("".join(lefts))
