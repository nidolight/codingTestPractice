def solution(N,adventurer):
    adventurer.sort()
    cnt = sum = 0
    
    for a in adventurer:
        sum+=1
        if sum == a:
            cnt+=1
            sum=0

    return cnt

print(solution(5,[2,3,1,1,2,2]))
