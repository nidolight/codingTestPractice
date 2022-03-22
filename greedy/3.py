def solution(string):
    result = ""
    result += string[0]
    for i in range(1, len(string)):#중복제거
        if string[i - 1] != string[i]:
            result += string[i]
    one = result.count('1')#1의 개수
    two = len(result) - one#0의 개수
    return min(one,two)

print(solution("00101100"))


