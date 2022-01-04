n = int(input())

for _ in range(n):
    s, e = map(int, input().split(' '))
    # 총 거리 : B지점 인덱스 - A지점 인덱스 - 1
    dist = (e - s)  # 남은 거리 (맨 처음 1칸 앞으로 움직인 경우는 먼저 반영한다.)

    cnt = 0  # default -> 맨 처음 1칸 움직인 경우에 대한 반영값

    next_choice = [1, 0, -1]
    while dist > 0:
        for d in next_choice:
            if (d-1)*d/2 <= dist - d:
                dist -= d
                next_choice = [d+1, d, d-1]
                cnt += 1
                break
    print(cnt)

