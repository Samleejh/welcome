min_human = 2
max_human = 10
total_human = 100
memo = {}

#트리 : 노드에 적은값 / 엣지에 적은 값
def divd(left, sit):
    key = str([left, sit])
    #종료조건
    if key in memo:
        return memo[key]
    if left < 0:            #성립X
        return 0
    if left == 0:           #유효한 경우
        return 1
    #재귀처리
    count = 0                                      #1번!!!
    for i in range(sit, max_human + 1):
        count += divd(left - i, i)
    #메모화 처리
    memo[key] = count
    #종료
    return count
print(divd(total_human, min_human))
