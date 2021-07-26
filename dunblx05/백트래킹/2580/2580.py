import sys

#입력
sdoku = [list(map(int, input().split())) for n in range(9)]

#0의 위치 기억
zero = [(i,j) for i in range(9) for j in range(9) if sdoku[i][j] == 0]

#가능성있는 숫자 검사
def is_promising(i,j):
    promising = [1,2,3,4,5,6,7,8,9]

    #행열 검사
    for k in range(9):
        if sdoku[i][k] in promising:
            promising.remove(sdoku[i][k])
        if sdoku[k][j] in promising:
            promising.remove(sdoku[k][j])

    i = i//3
    j = j//3

    # 3 * 3칸 검사
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sdoku[p][q] in promising:
                promising.remove(sdoku[p][q])

    return promising

flag = False

def backtracking(x):
    global flag

    # 정답이 나왔다면 종료
    if flag:
        return
    
    # 마지막 0까지 모두 다 채웠다면 정답 출력
    if x == len(zero):
        for row in sdoku:
            print(*row)
        flag = True
        return
    
    else:
        (i,j) = zero[x]
        promising = is_promising(i,j)   #가능한 숫자를 받아옴

        for num in promising:
            sdoku[i][j] = num           #가능한 숫자 중 하나를 넣은 후
            backtracking(x + 1)         #다음 0으로
            sdoku[i][j] = 0             #정답이 없을 경우 0으로 출력(틀린 입력이 들어온 경우 대비)

backtracking(0)