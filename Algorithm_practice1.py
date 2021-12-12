
# 재귀함수 - 팩토리얼
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

print(factorial(4))


# 재귀함수 - 피보나치 수열
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(1, 11):
    print(fib(i))


# 재귀함수 - 삼각수(자연수 1부터 n까지의 합)
def triangle_number(n):
    if n == 1:
        return 1
    return n + triangle_number(n-1)
print(triangle_number(4))


# 재귀함수 -  각 자릿수의 합
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print(sum_digits(22541))
print(sum_digits(92130))


# 재귀함수 - 리스트 거꾸로 뒤집기
def flip(alist):
    if len(alist) <= 1:
        return alist
    return alist[-1:] + flip(alist[:-1])

alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
alist = flip(alist)
print(alist)


# 재귀함수 - 이진 탐색
def binary_search(element, alist, start_index = 0, end_index = None):
    if end_index == None:
        end_index = len(alist) - 1

    if start_index > end_index:
        return None

    mid_index = (start_index + end_index) // 2

    if alist[mid_index] == element:
        return mid_index
    elif alist[mid_index] > element:
        return binary_search(element, alist, start_index, mid_index - 1)
    else:
        return binary_search(element, alist, mid_index + 1, end_index)

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))


# 재귀함수 - 하노이의 탑
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # base case: 옮길 원판이 없으면 부분 문제를 나누지 않고 함수를 끝낸다
    if num_disks == 0:
        return

    other_peg = 6 - start_peg - end_peg

    hanoi(num_disks - 1, start_peg, other_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, other_peg, end_peg)

hanoi(4, 1, 3)


# Brute Force의 장점
# 직관적이고 명확하다.
# 답을 확실하게 찾을 수 있다.

# Brutal force - 빗물 모으기(trapping rain)
def trapping_rain(buildings):

    lst_building = max(buildings)
    lst_idx = buildings.index(lst_building)

    left_idx = 0; left_max = buildings[0]
    right_idx = len(buildings) - 1; right_max = buildings[len(buildings) - 1]
    total_rain = 0

    # 가장 큰 기둥을 중심으로 왼쪽에 모인 빗물의 총량
    while left_idx != lst_idx:
        left_idx += 1
        if left_max <= buildings[left_idx]:
            left_max = buildings[left_idx]
        else:
            total_rain += left_max - buildings[left_idx]

    # 가장 큰 기둥을 중심으로 오른쪽에 모인 빗물의 총량
    while right_idx != lst_idx:
        right_idx -= 1
        if right_max <= buildings[right_idx]:
            right_max = buildings[right_idx]
        else:
            total_rain += right_max - buildings[right_idx]

    return total_rain

# test_set
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


# Divide and Conquer(분할정복)

# 분할정복 -  연속된 자연수의 합
def consecutive_sum(start, end):
    mid = (start + end) // 2
    if start == end:
        return mid
    return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)

print(consecutive_sum(10, 20))

# 분할 정복(Divide and Conquer)

# 분할정복 - 합병 정렬(merge sort)

# merge 함수 (정렬된 두 리스트를 받아서, 하나의 정렬된 리스트를 반환한다.)
def merge(list1, list2):

    merged_list = []
    i, j = 0, 0

    # 한 리스트에 있는 원소가 모두 merged_list에 들어갈 때까지 반복 (작은 수를 merged_list)에 append)
    while (i != len(list1)) and (j != len(list2)):

        if list1[i] >= list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    # 모든 원소가 merged_list에 들어가지 않은 리스트의 원소들을 마저 넣음
    merged_list += list1[i:]
    merged_list += list2[j:]

    # 합병된 리스트 리턴
    return merged_list

# merge sort
def merge_sort(alist):
    if len(alist) < 2:
        return alist

    mid = len(alist) // 2

    list1, list2 = alist[:mid], alist[mid:]
    list1 = merge_sort(list1)
    list2 = merge_sort(list2)

    return merge(list1, list2)

# test_case
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))


# 분할 정복 - 퀵 정렬(quick_sort)

def swap(alist, idx1, idx2):
    alist[idx1], alist[idx2] = alist[idx2], alist[idx1]

# 파티션 함수(pivot을 중심으로, pivot보다 작으면 왼쪽, 크면 오른쪽으로 위치 시킴)
def partition(alist, start, end):
    pivot = alist[end]; pivot_idx = end  # 맨 끝에 있는 원소가 pivot
    b = 0  # bigger_element

    for i in range(start, end):
        # 원소가 pivot보다 큰 경우, i만 1 증가
        # 작은 경우, b 위치에 있는 원소와 교체 후, b와 i 모두 1 증가
        if alist[i] < pivot:
            swap(alist, i, b)
            b += 1

    # 마지막으로 pivot과 b 위치에 있는 원소 자리 교체
    swap(alist, b, pivot_idx)
    pivot_idx = b
    return pivot_idx


# quick sort
def quick_sort(alist, start = 0, end = None):

    if end == None:
        end = len(alist) - 1

    # base_case
    if len(alist) <= 1:
        return alist

    p_idx = partition(alist, start, end)
    if len(alist[:p_idx]) != 0:
        alist[:p_idx] = quick_sort(alist[:p_idx], 0, len(alist[:p_idx]) - 1)
    if len(alist[p_idx + 1:]) != 0:
        alist[p_idx + 1:] = quick_sort(alist[p_idx + 1:], 0, len(alist[p_idx + 1:]) - 1)

    return alist

# test_case1
list1 = [1, 2, 5, 7, 9, 10, 13, 17]
quick_sort(list1)
print(list1)

# test_case2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 1, 1, 2, 15]
quick_sort(list2)
print(list2)


# 재귀함수 - 퀵 정렬
def quick_sort2(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1: return array

    pivot, tail = array[0], array[1:]

    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]

    return quick_sort2(leftSide) + [pivot] + quick_sort2(rightSide)


# Dynamic Programming
# 최적 부분 구조가 있다 : 부분 문제들의 최적의 답을 이용해서 기존 문제의 최적의 답을 구할 수 있다는 것
# -> 기존 문제를 부분 문제로 나눠서 풂 -> 중복되는 부분 문제들이 있을 수 있음.
# 중복 부분 문제

# 메모이제이션(Memoization)
# 하향식 접근(Top-down Approach)
# 재귀

# 메모이제이션 - 피보나치 수열
def fib_memo(n, cache):
    # base_case
    if n in cache:
        return cache[n]

    elif n < 3:
        return 1

    else:
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 1, cache)
        return cache[n]

def fib(n):
    fib_cache = {}
    return fib_memo(n, fib_cache)


# 타뷸레이션(Tabulation)
# 상향식 접근(Bottom-up Approach)
# 반복문

# 타뷸레이션 - 피보나치 수열
def fib_tab(n):
    # base_case
    fib_table = {1:1, 2:1}

    for i in range(1, n + 1):
        if i not in fib_table:
            fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n]

print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))


# 다이나믹 프로그래밍 - 공간 최적화
def fib_opt(n):
    previous = 1
    present = 1

    if n < 3:
        return 1

    for i in range(1, n - 1):
        previous, present = present, previous + present
    return present

print(fib_opt(3))


# 그리디 알고리즘(Greedy Algorithm)
# 미래를 내다보지 않고, 당장 눈 앞에 보이는 최적의 선택을 하는 방식
# 장점 : 간단하고 빠르다.
# 단점 : 최적의 답이 보장되지 않는다.

# 그리디 알고리즘이 최적의 답을 보장해주는 문제 (1, 2번 만족)
# 1. 최적 부분 구조일 때
# 2. 탐욕적 선택 속성(Greedy Choice Property) : 각 단계에서 탐욕스런 선택이 최종 답을 구하기 위한 최적의 선택이 될 때

# 그리디 알고리즘 - 최소 동전으로 거슬러주기
def min_coin_count(value, coin_list):

    coin_sum = 0
    for cost in sorted(coin_list, reverse = True):
        coin_sum += value // cost
        value %= cost
    return coin_sum

# base_case
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))