# sys.stdin.readline() 사용 시 input()에서의 rstrip() 과정이 없어 속도가 빠르다.
# 아스키 코드 출력 : ord()
# 문자열 split 후 리스트로 변환 : list(str)

# --------------------------------------------------------------------------------------------------------
# 백준 3052번
'''두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.'''

# 고유 개수 확인은 중복을 허용하지 않는 set(집합)을 사용한다.

a = set(int(input()) % 42 for i in range(10))
print(len(a))

# ----------------------------------------------------------------------------------
# 백준 4344번
'''첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.'''

# 퍼센트(%) 출력

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split(' ')))
    avg = sum(data[1:]) / data[0]
    over_avg = [i for i in data[1:] if i > avg]
    print(f'{(len(over_avg) / len(data[1:]))*100:.3f}%')

# --------------------------------------------------------------------------------------------------------
# 백준 1065
'''어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.'''

# 각 자릿수가 등차수열 -> 공차 일정

def han():
    n = int(input())
    if n < 100:
        return n
    else:
        _sum = 99

        for i in range(100, n + 1):
            li = list(map(int, list(str(i))))
            d = li[1] - li[0]
            prev = li[1]

            for j in li[2:]:
                if (j - prev) != d:
                    break
                else:
                    prev = j
                _sum += 1
        return _sum
print(han())

# --------------------------------------------------------------------------------------------------------
# 백준 1157번
'''첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.'''

# 딕셔너리 value 값 중 최댓값(중복) 리스트로 출력 / [k for k, v in d.items() if max(d.values()) == v]

d = dict()

data = list(input().lower())
for i in data:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

max_li = [k for k, v in d.items() if max(d.values()) == v]

if len(max_li) > 1:
    print('?')
else:
    print(max_li[0])

# --------------------------------------------------------------------------------------------------------
# 백준 2941번
'''입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.(목록에 없는 알파벳은 한 글자씩 센다.)'''

# 중복되는 값 제거 (예외)
d = {'c=':1, 'c-':1, 'dz=':1, 'd-':1, 'lj':1, 'nj':1, 's=':1, 'z=':1}
s = input()
tn = 0  # 크로아티아 알파벳 개수
tl = len(s)  # 남은 문자열 길이(개수)

for i in d.keys():
    if i in s:
        if (i == 'z=') and ('dz=' in s):  # 'dz=' 안에 'z='이 포함되므로, 중복되는 'z=' 제거
            tn += s.count(i) - s.count('dz=')
            tl -= len(i) * (s.count(i) - s.count('dz='))
        else:
            tn += s.count(i)
            tl -= len(i) * s.count(i)
print(tn + tl)

# --------------------------------------------------------------------------------------------------------
# 백준 1193
'''1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.'''

# 1부터 n까지의 합 : n(n+1)/2 (등차수열의 합)
def one_to_n(x):
    return int(x*(x+1)/2)

data = int(input())

def find_frac(x: int):
    i = 1

    while True:
        if x == 1:
            return '1/1'

        prev_ = one_to_n(i)
        next_ = one_to_n(i+1)

        if prev_ < x <= next_:
            if i % 2 != 0:  # 홀수
                return f'{x - prev_}/{next_ - x + 1}'
            else:  # 짝수
                return f'{next_ - x + 1}/{x - prev_}'

        else:
            i += 1

print(find_frac(data))

# --------------------------------------------------------------------------------------------------------
# 백준 2869
'''땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.'''

# 조건과 반올림(올림)
from math import ceil

# climb * i - slide(i - 1) > total

climb, slide, height = map(int, input().split(' '))
print(ceil((height - slide) / (climb - slide)))

# --------------------------------------------------------------------------------------------------------
# 백준 10757번

# 큰 수의 덧셈 -> 덧셈의 원리 적용
l1, l2 = input().split(' ')

def add_large(l1, l2):
    data = ''
    p = 0

    # 길이를 동일하게 해준다.
    if len(l1) > len(l2):
        l2 = l2.zfill(len(l1))
    elif len(l1) < len(l2):
        l1 = l1.zfill(len(l2))

    # 각 자릿수 별 합
    for i in range(len(l1)-1, -1, -1):
        s = int(l1[i]) + int(l2[i]) + p
        p = s // 10  # 합이 10을 넘어가면, p에다 1을 더한다. -> 다음 자릿수 합 연산에 적용
        data = str(s % 10) + data
    if p != 0:  # p가 1일 경우, 맨 앞자리에 1 추가
        data = str(p) + data

    return int(data)

print(add_large(l1, l2))

# --------------------------------------------------------------------------------------------------------
# 백준 1011번
'''
이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다.
예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 
사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로, 1 광년을 이동할 수 있으며
그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다.
...
공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다. 
하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.
김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라.'''

# 아이디어 -> n만큼 이동하려면 최소한 (n-1)*n/2 의 거리는 남아있어야 한다.
n = int(input())

for _ in range(n):
    s, e = map(int, input().split(' '))
    # 총 거리 : B지점 인덱스 - A지점 인덱스 - 1
    dist = (e - s)  # 남은 거리 (초깃값 : 총 이동거리)
    cnt = 0  # 이동 횟수

    next_choice = [1, 0, -1]  # 선택지
    while dist > 0:
        for d in next_choice:
            if (d-1)*d/2 <= dist - d:  # 아이디어 적용
                dist -= d  # 남은 거리 갱신
                next_choice = [d+1, d, d-1]  # 선택지 갱신
                cnt += 1
                break

    print(cnt)