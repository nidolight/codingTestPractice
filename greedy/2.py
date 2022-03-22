def solution(string):
    tmp = ""
    for c in string:
        if int(c) == 0:
            tmp+=c+'+'
        else:
            tmp+=c+'*'
    # print(tmp)
    return eval(tmp[:-1])

print(solution("02984"))
print(solution("567"))
