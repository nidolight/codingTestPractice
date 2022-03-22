def solution(N,M,weights):
    w = [0] * (M+1)

    for i in weights :
    # 각 무게에 해당하는 볼링공의 개수
        w[i] += 1

    answer = 0
    # 1부터 m까지의 각 무게에 대하여 처리
    for i in range(1, M + 1) :
        # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
        N -= w[i]
        # B가 선택하는 경우의 수와 곱하기
        answer += w[i] * N

    return answer

print(solution(5,3,[1,3,2,3,2]))