
def solution(N,coins):
    coins.sort()
    answer = 1

    for coin in coins:
        #print(coin,answer)
        if coin > answer :
            break
        answer += coin

    return answer

print(solution(5,[3,2,1,1,9]))
