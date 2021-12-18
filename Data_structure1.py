'''
### 파이썬 자료구조
# 자료 구조의 목적 : 데이터를 효율적으로 저장하고, 저장한 데이터를 효율적으로 찾는 것

## 배열(Array)

# C 배열 : 1) 데이터가 메모리에 연속적으로 저장 2) 크기가 고정되어 있다 3) 같은 타입의 데이터만 담을 수 있다.
# 파이썬 리스트 : 레퍼런스가 메모리에 연속적으로 저장 (실제 값들은 레퍼런스를 따라가면 나온다)

alist = [1, 2, 3, 4, 5]
for i in alist:
    print(id(i))

# alist의 원소들의 레퍼런스 : 2609353523440, 2609353523472, 2609353523504, 2609353523536, 2609353523568
# 위 메모리 주소들은 2609353523440 + 32n (n >= 0)로 일반화할 수 있다.(2609353523440 : 첫째 항, n : 인덱스, 32 : 데이터의 크기)
# 인덱스(n)가 정해짐에 따라, 레퍼런스도 "바로" 정해진다. -> 배열 접근 연산 : O(1)

# 배열 탐색 연산 : 선형 탐색 -> O(n)

# 정적 배열(Static Array) : 크기 고정(요소 수 제한) / 동적 배열(Dynamic Array) : 크기 변함(요소 계속 추가 가능)

# 동적 배열
# 내부적으로는 정적 배열로 만들어진 자료구조(배열의 크기를 상황에 맞게 조절)
# ex) 4개의 원소를 담을 수 있게 정의된 배열에 다섯 번째 원소가 들어감
# -> 그 2배인 8개의 원소를 담을 수 있는 배열이 들어갈 만한 메모리를 다시 찾아서, 기존의 배열을 복붙하고, 새로 들어온 원소를 뒤에 추가

# 동적 배열의 추가(append) 연산 :
# 경우 1) 정적 배열에 남는 공간이 있을 때 : 최고의 경우 O(1)
# 경우 2) 정적 배열이 꽉 찼을 때 : 최악의 경우 O(n)

# 분할 상환 분석(Amortized Analysis)
# 주어진 알고리즘의 시간 복잡도나 프로그램을 수행하는데 소요되는 시간 또는 메모리 같은 자원 사용량을 분석하기 위해 사용하는 기법.
# 전반적인 연산 집합에 대해 비용이 높은 연산, 비용이 덜한 연산 모두를 함께 고려하는 기법.
# 수행된 모든 연산에 대해 자료구조 연산만의 어떤 시퀀스를 수행하는데 필요한 시간의 평균을 구한다.

# 동적 배열의 추가 연산 : 분할 상환 분석 시, 시간 복잡도 O(1)

# 동적 배열의 삽입 연산 :
# 경우 1) 정적 배열에 남는 공간이 있을 때 : O(n) (맨 끝에 추가 : O(1))
# 경우 2) 정적 배열이 꽉 찼을 때 : O(n)

# 동적배열의 삭제 연산 :
# 최고의 경우(맨 끝 데이터를 지우는 경우) : O(1), 최악의 경우 : O(n)
# 맨 끝 데이터를 지우는 경우에도, 동적배열의 크기가 줄어드는 과정에서(메모리 낭비 최소화) O(n)이 될 수도 있지만, 분할 상환 분석에 따라 O(1)이 된다.


## 연결 리스트(Linked List)
# 추상적 자료형인 리스트를 구현한 자료구조
# 데이터를 순서대로 저장해준다.
# 요소를 계속 추가할 수 있다.
# 배열에 비해 데이터의 추가/삽입 및 삭제가 용이하나, 순차적으로 탐색하지 않으면 특정 위치의 요소에 접근할 수 없어 일반적으로 탐색 속도가 떨어진다.
# 즉 탐색, 정렬을 자주 하면 배열을, 추가/삭제가 많으면 연결리스트를 사용하는 것이 유리하다.

class Node:
    """연결 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 데이터
        self.next = None  # 다음 노드의 레퍼런스
        # Doubly linked list
        self.prev = None  # 이전 노드의 레퍼런스


class LinkedList:
    """연결 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """연결 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = ""

        iterator = self.head  # 연결 리스트 안의 모든 노드를 순회하기 위한 변수

        while iterator.next is not None:
            res_str += f"{iterator.data}->"
            iterator = iterator.next
        res_str += f"{iterator.data}"

        return res_str

    def append(self, data):
        """연결 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:  # 연결 리스트가 비어 있는 경우
            self.head = new_node
            self.tail = new_node
        else:  # 연결 리스트가 비어 있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node

    def get_node_at(self, index):
        """연결 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정."""
        iterator = self.head

        for i in range(index):
            iterator = iterator.next

        return iterator

    def insert_after(self, previous_node, data):
        """연결 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)

        if previous_node is self.tail:  # 맨 뒤에 삽입하는 경우
            previous_node.next = new_node
            self.tail = new_node
        else:  # 두 노드 사이에 삽입하는 경우
            new_node.next = previous_node.next
            previous_node.next = new_node

    # Singly linked list는 이전 노드의 레퍼런스를 가리키는 prev가 없어서 insert_before 메소드 구현이 어렵다.
    def prepend(self, data):
        """연결 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)

        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node

    def del_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        if self.get_node_at(index) is self.tail:
            self.tail = self.get_node_at(index-1)
        self.get_node_at(index-1).next = self.get_node_at(index).next


# 이중 연결 리스트의 시간 복잡도
# 접근 : O(n) / 탐색 : O(n) / 삽입 O(1) / 삭제 O(1) (원하는 노드에 접근 또는 탐색 + 삽입/삭제 : O(n))
# 단일 연결 리스트와 이중 연결 리스트의 tail 노드 삭제 시간 복잡도 : O(n) / O(1)
# 단일 연결 리스트와 이중 연결 리스트의 레퍼런스 저장 공간 복잡도 차이 -> 2배 정도
class DoublyLinkedList:
    """이중 연결 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """연결 리스트를 문자열로 표현해서 리턴하는 메소드(연결 리스트도 동일)"""
        res_str = ""

        iterator = self.head  # 연결 리스트 안의 모든 노드를 순회하기 위한 변수

        while iterator.next is not None:
            res_str += f"{iterator.data}<->"
            iterator = iterator.next
        res_str += f"{iterator.data}"

        return res_str

    def append(self, data):
        """이중 연결 리스트 추가 연산 메소드"""
        new_node = Node(data)  # 새로운 데이터를 저장하는 노드

        if self.head is None:  # 이중 연결 리스트가 비어있는 경우
            self.head = new_node
            self.tail = new_node
        else:  # 이중 연결 리스트에 데이터가 이미 있는 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def get_node_at(self, index):
        """이중 연결 리스트 접근 연산 메소드(연결 리스트도 동일)"""
        iterator = self.head

        for i in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다.(연결 리스트도 동일)"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next

        return None

    def insert_after(self, previous_node, data):
        """연결 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)

        if previous_node is self.tail:  # 맨 뒤에 삽입하는 경우
            previous_node.next = new_node
            new_node.prev = previous_node
            self.tail = new_node
        else:  # 두 노드 사이에 삽입하는 경우
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def insert_before(self, former_node, data):
        """연결 리스트 주어진 노드 앞 삽입 연산 메소드(prepend 상위 호환, 사실상 insert 메소드에 가까움.)"""
        new_node = Node(data)

        if former_node is self.head:  # 맨 앞에 삽입하는 경우
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:  # 두 노드 사이에 삽입하는 경우
            new_node.next = former_node
            new_node.prev = former_node.prev
            former_node.prev.next = new_node
            former_node.prev = new_node

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""
        if node_to_delete is self.head and node_to_delete is self.tail:  # 하나 남은 노드를 지우는 경우
            self.head = None
            self.tail = None
        elif node_to_delete is self.head:  # 맨 앞의 노드를 지우는 경우
            self.head = self.head.next
            self.head.prev = None
        elif node_to_delete is self.tail:  # 맨 뒤의 노드를 지우는 경우
            self.tail = self.tail.prev
            self.tail.next = None
        else:  # 두 노드 사이에 있는 노드를 지우는 경우
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prevㄴ
            
            
# 노드 생성 및 데이터 할당
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(8)
tail_node = Node(13)

# 노드 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

# 노드들을 순서대로 출력
iterator = head_node
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

linked = LinkedList()
linked.head = head_node
linked.tail = tail_node

linked.append(21)  # 추가 연산

print(linked.tail.data)
print(linked.head.data)
print(linked)  # __str__ 함수 실행

linked.get_node_at(3).data = 11  # 연결 리스트 노드에 접근(데이터 바꾸기)
print(linked)

linked.insert_after(node_3, 12)  # 주어진 노드 다음 삽입 연산
print(linked)

linked.del_node(5)  # 해당 인덱스에 있는 노드 제거 연산
linked.del_node(5)
print(linked)

# 노드 생성 및 데이터 할당
doubly_linked = DoublyLinkedList()
doubly_linked.append(2)
doubly_linked.append(3)
doubly_linked.append(5)
doubly_linked.append(8)
doubly_linked.append(13)
print(doubly_linked)

prev_node = doubly_linked.get_node_at(3)
doubly_linked.insert_after(prev_node, 10)  # 주어진 노드 다음 삽입 연산
print(doubly_linked)

form_node = doubly_linked.get_node_at(3)
doubly_linked.insert_before(form_node, 7)  # 주어진 노드 이전 삽입 연산(사실상 삽입 연산)
doubly_linked.insert_before(doubly_linked.head, 1)
print(doubly_linked)

del_node = doubly_linked.get_node_at(3)
doubly_linked.delete(del_node)  # 주어진 노도 삭제 연산
print(doubly_linked)


## 해시 테이블(Hash Table)
# 하나의 key와 그 key에 해당하는 value를 합쳐서 : key-value 쌍
# 하나의 key에는 하나의 value 만 있어야 한다.

# 배열 인덱스 접근 : O(1) (인덱스를 key로 생각하고 데이터 저장)
# Direct Access Table : 가장 간단한 형태의 해시테이블. 키 값을 주소로 사용하는 테이블. 키 값이 100이라고 했을 때, 배열의 인덱스 100에 원하는 데이터를 저장하는 것
# 장점 : 1) 탐색, 삽입, 삭제 연산을 모두 O(1)에 할 수 있다. 2) 최대 키 값이 작을 때, 실용적인 사용이 가능하다.
# 단점 : 1) 최대 키 값에 대해 알고 있어야 한다. 2) 키 값의 분산이 크다면, 메모리 낭비가 심할 수 밖에 없다.

# 해시 함수 : key를 해시(Hash)로 변경해주는 함수
# 해시(Hash) : 인풋 데이터를 해싱을 통해 고정된 길이의 숫자열로 변환한 결과물
# 해시 테이블(Hash Table) -> 1) 고정된 크기의 배열을 만든다. 2) 해시 함수를 이용해서 key를 원하는 범위의 자연수로 바꾼다.(해싱) 3) 해시 함수 결과 값 인덱스에 key-value 쌍을 저장한다.

# 해시 함수 조건 : 1) 결정론적이어야 한다. 2) 원하는 범위의 자연수 하나 하나가 리턴될 확률이 최대한 비슷해야 한다. 3) 빠른 계산이 가능해야 한다.

# 파이썬 hash 함수 : 파라미터로 받은 값을 그냥 아무 정수로 바꿔준다. (hash 함수에 서로 다른 두 값을 파라미터로 넣었을 때, 같은 정수가 리턴될 수 없다.)
print(hash("파이썬"))
print(hash(12.15))
# print(hash([1,2,3]))는 오류가 난다. 왜냐하면, hash 함수는 언어 자체적으로 "불변 타입 자료형"에만 사용이 가능하기 때문!

# 해시 충돌 : 해시 함수가 서로 다른 두 개의 입력값에 대해 동일한 출력값을 내는 상황
# 해시 함수가 무한한 가짓수의 입력값을 받아 유한한 가짓수의 출력값을 생성하는 경우, 비둘기집 원리에 의해 해시 충돌은 항상 존재한다.

## 체이닝(Chaining) : 배열 내에 연결 리스트를 할당하여, 배열에 데이터를 삽입하다가, 해시 충돌이 발생하면 연결 리스트로 데이터들을 연결하는 방법

class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def find_node_with_key(self, key):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.key == key:
                return iterator

            iterator = iterator.next

        return None

    def append(self, key, value):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(key, value)

        # 빈 링크드 리스트라면 head와 tail을 새로 만든 노드로 지정
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 이미 노드가 있으면
        else:
            self.tail.next = new_node  # 마지막 노드의 다음 노드로 추가
            new_node.prev = self.tail
            self.tail = new_node  # 마지막 노드 업데이

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""

        # 링크드 리스트에서 마지막 남은 데이터를 삭제할 때
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None

        # 링크드 리스트 가장 앞 데이터 삭제할 때
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        # 링크드 리스트 가장 뒤 데이터 삭제할 떄
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # 두 노드 사이에 있는 데이터 삭제할 때
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.value

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = ""

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str

# Chaining을 쓰는 해시 테이블 탐색 연산
# 1) 해시 함수 계산 2) 배열의 Hash 인덱스에 해당하는 연결 리스트에 접근 3) 연결 리스트에서 key에 해당하는 value 탐색

# Chaining을 쓰는 해시 테이블 삽입 연산
# 1) 해시 함수 계산 2) 배열 인덱스 접근 3) 연결 리스트 노드 탐색(key가 있는지 없는지 확인) 4) 연결 리스트 저장 / 노드 수정
# 1) 해시 함수 계산 2) 배열 인덱스 접근 3) 연결 리스트 노드 탐색(key가 있는지 없는지 확인) 4) 연결 리스트 저장 / 노드 수정

# Chaining을 쓰는 해시 테이블 삭제 연산
# 1) 해시 함수 계산 2) 배열 인덱스 접근 3) 연결 리스트 노드 탐색(key가 있는지 없는지 확인) / 연결 리스트 노드 삭제

# 해시 테이블 평균 시간 복잡도 -> 탐색 : O(1) / 저장 : O(1) / 삭제 : O(1)  (한 해시에 모든 데이터가 들어있는 경우(최악의 경우) : O(n))

class HashTable:
    """해시 테이블 클래스"""

    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용 크기 저장
        self._table = [LinkedList() for _ in range(self._capacity)]  # 파이썬 리스트 인덱스에 반 링크드 리스트 저장

    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]

    def _hash_function(self, key):
        """
        주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        주의: key는 파이썬 불변 타입이여야 한다.
        """
        return hash(key) % self._capacity

    def _get_linked_list_for_key(self, key):
        """주어진 key에 대응하는 인덱스에 저장된 링크드 리스트를 리턴하는 메소드"""
        hashed_index = self._hash_function(key)
        return self._table[hashed_index]

    def _look_up_node(self, key):
        """파라미터로 받은 key를 갖고 있는 노드를 리턴하는 메소드"""
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)

    def look_up_value(self, key):
        """
        주어진 key에 해당하는 데이터를 리턴하는 메소드
        """
        return self._look_up_node(key).value

    def insert(self, key, value):
        """
        새로운 key - value 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔준다
        """
        existing_node = self._look_up_node(key)
        linked_list = self._get_linked_list_for_key(key)
        if existing_node is None:
            linked_list.append(key, value)
            return
        existing_node.value = value

    def delete_by_key(self, key):
        """주어진 key에 해당하는 key - value 쌍을 삭제하는 메소드"""
        linked_list = self._get_linked_list_for_key(key)
        node_to_delete = self._look_up_node(key)
        linked_list.delete(node_to_delete)


test_scores = HashTable(50)  # 시험 점수를 담을 해시 테이블 인스턴스 생성

# 여러 학생들 이름과 시험 점수 삽입
test_scores.insert("현승", 85)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
test_scores.insert("지웅", 99)
test_scores.insert("신의", 88)
test_scores.insert("규식", 97)
test_scores.insert("태호", 90)

print(test_scores)

# key인 이름으로 특정 학생 시험 점수 검색
print(test_scores.look_up_value("현승"))
print(test_scores.look_up_value("태호"))
print(test_scores.look_up_value("영훈"))

# 학생들 시험 점수 수정
test_scores.insert("현승", 10)
test_scores.insert("태호", 20)
test_scores.insert("영훈", 30)

print(test_scores)


## 개방 주소법(Open Addressing)
# 체이닝의 경우, 배열이 꽉 차더라도, 연결리스트로 계속 늘려가기에, 데이터의 주소값은 바뀌지 않는다.
# 개방 주소법의 경우, 해시 충돌이 일어나면, 다른 버켓에 데이터를 삽입한다.

# 선형 탐색(Linear Probing) : 해시 충돌 시, 빈 인덱스를 하나씩 순서대로 선형적으로 찾아 데이터를 삽입한다.
# 제곱 탐색(Quadratic Probing) : 해시 충돌 시, 빈 인덱스를 제곱만큼 건너뛰며 찾아 데이터를 삽입한다.
# 이중 해시(Double Hashing) 해시 충돌 시, 다른 해시함수를 한 번 더 적용한 결과를 이용한다.

class OpenAddressing:
    """해시 테이블(Open Addressing 방법 이용) 클래스"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_table = [0 for i in range(self.capacity)]

    def get_key(self, data):
        """아스키 코드로 된 키 값을 반환하는 메소드"""
        self.key = ord(data[0])  # ord() 함수 : 특정한 한 문자를 아스키 코드 값으로 변환해주는 함수
        return self.key

    def hash_function(self, key):
        """해시 함수"""
        return key % self.capacity

    def get_address(self, key):
        """해시 값(주소)를 반환하는 함수"""
        myKey = self.get_key(key)
        hash_address = self.hash_function(myKey)
        return hash_address

    def save(self, key, value):
        """key-value 쌍을 저장 및 수정하는 메소드"""
        hash_address = self.get_address(key)

        # Linear Probing
        if self.hash_table[hash_address] != 0:  # 해시에 해당하는 버켓이 차 있는 경우
            for i in range(hash_address, len(self.hash_table)):  # 한 칸씩 이동하면 빈 버켓 탐색
                if self.hash_table[i] == 0:  # 버켓이 비어있는 경우
                    self.hash_table[i] = [key, value]
                    return
                elif self.hash_table[i][0] == key: # 버켓에 이미 key 값이 들어있는 경우
                    self.hast_table[i] = [key, value]
                    return
            return None  # 빈 공간이 없는 경우
        else:  # 해시에 해당하는 버켓이 비어 있는 경우
            self.hash_table[hash_address] = [key, value]

    def read(self, key):
        """key에 해당하는 value값을 반환하는 메소드"""
        hash_address = self.get_address(key)

        for i in range(hash_address, len(self.hash_table)):  # Linear Probing을 하며, key에 해당하는 value를 반환
            if self.hash_table[i][0] == key:  # 해당하는 key 값이 있는 경우
                return self.hash_table[i][1]
        return None  # 해당하는 key 값이 없는 경우 -> None 반환

    def delete(self, key):
        """key에 해당하는 key-value 쌍을 삭제하는 메소드"""
        hash_address = self.get_address(key)

        for i in range(hash_address, len(self.hash_table)):
            if self.hash_table[i] == 0:
                continue
            if self.hash_table[i][0] == key:  # 해당하는 key 값이 있는 경우
                self.hash_table[i] = 0
                return
        return False  # 해당하는 key 값이 없는 경우


h_table = OpenAddressing(10)

data1 = 'aa'
data2 = 'ab'
data3 = 'bb'
print(ord(data1[0]), ord(data2[0]))

h_table.save('1a', '123')
h_table.save('2b', '456')
h_table.save('3b', '789')

print(h_table.hash_table)

print(h_table.read('1a'))

h_table.delete('1a')
print(h_table.hash_table)

# 체이닝(Chaining)의 장점
# 1) 연결 리스트만 사용하면 된다. 즉, 복잡한 계산식을 사용할 필요가 개방주소법에 비해 적다.
# 2) 해시테이블이 채워질수록, Lookup 성능저하가 Linear하게 발생한다.

# 개방 주소법(Open Addressing)의 장점
# 1) 체이닝 처럼 포인터가 필요 없고, 지정한 메모리 외 추가적인 저장 공간도 필요 없다.
# 2) 삽입, 삭제 시 오버헤드가 적다.(오버헤드 : 어떤 처리를 하기 위해 들어가는 간접적인 처리 시간, 메모리 등)
# 3) 저장할 데이터가 적을 때 더 유리하다.

# load factor a (테이블이 얼마나 차 있는지를 나타내는 변수)
# a = n/m (n : 해시 테이블 안에 들어있는 데이터 쌍 수 / m : 해시 테이블이 사용하는 배열의 크기) (a <= 1)

# Open addressing을 사용하는 해시 테이블에서 평균적으로 탐사를 해야되는 횟수(기댓값)은 1/(1-a)보다 작다.
# 배열이 총 100칸이고, 90개의 key-value 쌍을 저장했다고 할 때, load factor a = 0.9인데,
# 기댓값에 a를 대입하면 10이 나온다. 즉, 빈 인덱스를 찾기 위해서 평균적으로 인덱스 10개보다 적은 인덱스를 확인해도 된다는 뜻 : O(10) -> 평균적으로 O(1)

# Chaining을 사용하든 Open addressing을 사용하든, 해시 테이블의 모든 연산(삽입, 탐색, 삭제)을 평균적으로 O(1)에 할 수 있다.


## 추상 자료형(Abstract Data Type) : 자료구조를 추상화 한 것 / 데이터를 저장, 사용할 때 기능만 생각(구현은 생각x)


# deque(Doubly-ended-queue)
# 맨 앞과 뒤에 데이터를 삽입하고 삭제할 수 있게 해주는 자료형
from collections import deque


## 큐(Queue)
# FIFO(First-in-first-out)
# 맨 뒤 데이터 추가, 맨 앞 데이터 삭제, 맨 앞 데이터 접근
queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("A")
queue.append("B")
queue.append("C")
queue.append("D")

print(queue)  # 큐 출력

print(queue[0])  # 큐의 맨 앞 데이터에 접근

print(queue.popleft())  # 큐 맨 앞 데이터 리턴 및 삭제


## 스택(Stack)
# LIFO(Last-in-first-out)
# 맨 뒤 데이터 추가, 맨 뒤 데이터 삭제, 맨 뒤 데이터 접근
stack = deque()

# 큐의 맨 끝에 데이터 삽입
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")

print(stack)  # 스택 출력

print(stack[-1])  # 스택의 맨 끝 데이터에 접근

print(stack.pop())  # 스택의 맨 끝 데이터 리턴 및 삭제


## 세트(Set)
# 집합을 표현(합집합, 교집합, 차집합 등의 연산이 가능)
# 중복된 값을 허용하지 않는다.
# 순서가 보장되지 않는다.(인덱스도 존재하지 않음)
set1 = {"A", "B", "C"}
set1.add("A")
set1.add("D")
set1.add("E")

print(set1) # 세트 출력

print("A" in set1)  # 데이터 탐색

set1.remove("C")  # 데이터 삭제

print(set1)

## 파이썬 주요 추상 자료형 시간 복잡도 정리

# 1. 리스트(동적배열)
# 접근 : O(1) / 추가 : O(1) (분할 상환) / 맨 뒤 삭제 O(1) (분할 상환) / 길이 확인 : O(1) / 삽입 : O(n) / 삭제 : O(n) / 탐색 : O(n)

# 2. deque(이중 연결 리스트)
# 맨 앞 삭제 : O(1) / 맨 앞 삽입 : O(1) / 맨 뒤 삭제 : O(1) / 맨 뒤 삽입 : O(1) / 길이 확인 : O(1)

# 3. 딕셔너리(해시 테이블)
# 탐색 : O(1) (평균) / 삽입 : O(1) (평균) / 삭제 : O(1) (평균) / 길이 확인 : O(1)

# 4. 세트(해시 테이블)
# 탐색 : O(1) (평균) / 삽입 : O(1) (평균) / 삭제 : O(1) (평균) / 길이 확인 : O(1)


## 트리
# 데이터의 상-하 관계(계층적 관계)를 저장하는 자료구조
# 다양한 추상 자료형의 구현이 가능 ex) 우선순위 큐, 딕셔너리, 세트 등

# 루트(start) 노드 : 트리의 시작 노드
# 부모 노드 : 특정 노드의 직속 상위 노드
# 자식 노드 : 특정 노드의 직속 하위 노드
# 형제 노드 : 같은 부모를 갖는 노드
# leaf 노드(말단 노드) : 자식 노드를 갖고 있지 않은, 가장 말단에 있는 노드
# 깊이 : 특정 노드가 start 노드에서 떨어져 있는 거리 (start 노드의 자식 노드의 깊이는 1)
# 레벨 : 깊이 + 1. 깊이와 거의 같은 개념 (start 노드의 자식 노드의 레벨은 2)
# 높이 : 트리에서 가장 깊이 있는 노드의 깊이
# 부분 트리(sub-tree) : 현재 트리의 일부분을 이루고 있는 더 작은 트리


## 이진 트리
# 각 노드가 최대 2개의 자식 노드를 가질 수 있는 트리

class Node:
    """이진 트리 노드 클래스"""

    def __init__(self,data):
        """데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None


# 데이터 할당
root_node = Node(2)
node_B = Node(3)
node_C = Node(5)
node_D = Node(8)
node_E = Node(13)

# 노드 지정
root_node.left_child = node_B
root_node.right_child = node_C
node_B.left_child = node_D
node_B.right_child = node_E

# start 노드의 왼쪽 자식 노드 가져오기
test_node_1 = root_node.left_child
print(test_node_1.data)


# 정 이진 트리(Full Binary Tree)
# 모든 노드가 모든 노드가 2개 도는 0개의 자식을 갖는 이진 트리

# 완전 이진 트리(Complete Binary Tree)
# 마지막 레벨 직전의 레벨까지는 모든 노드들이 다 채워진 트리
# 조건 : 마지막 레벨에서는 노드들이 다 채워질 필요는 없더라도, 왼쪽부터 오른쪽 방향으로는 노드들이 다 채워져야 한다.
# 성질 : 완전 이진 트리 안에 저장된 노드가 n개라고 할 때, 높이는 항상 log(n)에 비례한다.

# 포화 이진 트리(Perfect Binary Tree)
# 모든 레벨이 빠짐 없이 노드로 채워져 있는 이진 트리
# 완전 이진 트리와, 정 이진 트리의 특성을 모두 갖는다.
# n + 1 = 2^(h+1) (n : 노드의 수, h : 높이)


# 완전 이진 트리 배열(파이썬 리스트)에 저장하기
complete_binary_tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]  # 첫 번째 인덱스 : start 노드

# 완전 이진 트리 배열 자식 노드 찾는 방법
# 2p (p : 부모 노드의 인덱스)
# 2p + 1 (p : 부모 노드의 인덱스)

# 완전 이진 트리 배열 부모 노드 찾는 방법
# c // 2 (c : 자식 노드의 인덱스)

def get_parent(complete_binary_tree: list, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 부모 노드의 데이터 리턴"""
    return complete_binary_tree[index // 2] if index != 0 else None  # start 노드일 경우, None 리턴

def get_left_child(complete_binary_tree: list, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 왼쪽 자식 노드의 데이터 리턴"""
    return complete_binary_tree[index * 2] if index * 2 <= len(complete_binary_tree) else None  # 배열을 넘어가는 경우, None을 리턴

def get_right_child(complete_binary_tree: list, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 오른쪽 자식 노드의 데이터 리턴"""
    return complete_binary_tree[index * 2 + 1] if index * 2 + 1 <= len(complete_binary_tree) else None  # 배열을 넘어가는 경우, None을 리턴


# 순회
# 자료 구조에 저장된 모든 데이터를 도는 것

# 트리 순회
# 트리를 순회하면 노드들 사이에 선형적 순서를 만들 수 있다.

# 1.pre-order 순회
# 1) 현재 노드 데이터 출력
# 2) 재귀적으로 왼쪽 부분 트리 순회
# #) 재귀적으로 오른쪽 부분 트리 순회

# 2.post-order 순회
# 1) 재귀적으로 왼쪽 부분 트리 순회
# 2) 재귀적으로 오른쪽 부분 트리 순회
# 3) 현재 노드 데이터를 출력

# 3.in-order 순회
# 1) 재귀적으로 왼쪽 부분 트리 순회
# 2) 현재 노드 데이터를 출력
# 3) 재귀적으로 오른쪽 부분 트리 순회

class Node:
    """이진 트리 노드 클래스"""

    def __init__(self,data):
        """데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None

# 노드 생성
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")
node_I = Node("I")

# 생성한 노드 인스턴스 연결
node_F.left_child = node_B  # node_F : 루트 노드
node_F.right_child = node_G

node_B.left_child = node_A
node_B.right_child = node_D

node_D.left_child = node_C
node_D.right_child = node_E

node_G.right_child = node_I

node_I.left_child = node_H

def traverse_in_order(node):
    """in-order 순회 함수"""
    res_str = ""

    if node.left_child is not None:  # 왼쪽 부분 트리 순회
        traverse_in_order(node.left_child)

    print(node.data, end = ' ')  # 데이터 출력

    if node.right_child is not None:  # 오른쪽 부분 트리 순회
        traverse_in_order(node.right_child)

traverse_in_order(node_F)  # 루트 노드부터 in-order 순회


## 힙(Heap)
# 형태 속성 : 힙은 완전 이진 트리다.
# 힙 속성 : 모든 노드의 데이터는 자식 노드들의 데이터보다 크거나 같다.

def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 서로 바꾼다."""
    tree[index_1], tree[index_2] = tree[index_2], tree[index_1]

# heapify 함수 실행 시간 복잡도 : O(log(n))
def heapify(tree, index, tree_size):
    """heapify 함수"""

    left_child_index = 2 * index  # 왼쪽 자식 노드 인덱스
    right_child_index = 2 * index + 1  # 오른쪽 자식 노드 인덱스

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index


    if largest != index:  # 부모 노드의 값이 자식 노드의 값보다 작은 경우,
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 서로 바꾼다.
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를 대상으로 다시 heapfiy 함수를 호출한다. (힙 속성이 충족될 때까지 반복)

test_tree = [None, 3,1,7, 12, 9, 13, 8, 6, 17, 2]


# 힙 만드는 법
# 마지막 인덱스부터 루트 노드의 인덱스까지 순서대로 heapify 함수를 실행한다.
# 힙 만드는 과정 시간복잡도 : O(nlog(n))

def making_heap(tree):
    tree_size = len(test_tree)
    for idx in range(tree_size - 1, 0, -1):  # O(n)
        heapify(tree, idx, tree_size)  #O (log(n))

print(test_tree) # 힙으로 만들어진 트리 출력


## 힙 정렬(Heap sort)
# 힙을 이용한 정렬 알고리즘 (시간 복잡도 : O(nlog(n)))
# 1) 힙을 만든다.
# 2) root와 마지막 노드를 바꿔준다.
# 3) 바꾼 노드는 없는 노드 취급한다.
# 4) 새로운 노드가 힙 속성을 지킬 수 있게 heapify 함수를 호출한다.
# 5) 2 ~ 4번 과정을 모든 인덱스를 돌 때까지 반복한다.

# 내림차순으로 정렬하고 싶을 경우-> 힙 속성을 반대로 바꾸고 똑같은 알고리즘을 적용하면 된다.

def heap_sort(tree):
    """힙 정렬(heap_test_1-sort) 메소드"""
    tree_size = len(tree)

    making_heap(tree) # 1번 과정

    for i in range(tree_size - 1, 0, -1):  # 2 ~ 5번 과정
        swap(tree, 1, i)
        heapify(tree, 1, i)
    print(tree)  # 힙 정렬된 트리 출력


# test_code
test_tree = [None, 3, 1, 7, 12, 9, 13, 8, 6, 17, 2]
heap_sort(test_tree)


## 우선순위 큐
# 추상 자료형(내부적인 구현보다 기능에 집중하게 해주는 개념) 중 하나
# 데이터를 저장할 수 있다.
# 저장한 데이터가 우선 순위 순서대로 나온다.
from queue import PriorityQueue

priority_queue = PriorityQueue()  # 우선 순위에 있는 값이 작을수록 먼저 출력
priority_queue.put((3, "철수"))  # 우선 순위 큐에 원소 추가
priority_queue.put((1, "영희"))
priority_queue.put((2, "민수"))
priority_queue.put((6, "유리"))
priority_queue.put((5, "민아"))
priority_queue.put((4, "준수"))

print(priority_queue.queue)  # 우선 순위 큐에 있는 원소들 출력
print(priority_queue.get())  # 우선 순위 큐에 원소 삭제
print(priority_queue.queue)


# 힙에 데이터 삽입하기
# 1) 힙의 마지막 인덱스에 데이터를 삽입한다.
# 2) 삽입한 데이터와 부모 노드의 데이터를 비교한다.

# 힙에서 최고 우선순위 데이터 추출하기 (최고 우선 순위 : 가장 큰 데이터(root_node의 데이터))
# 1) start 노드와 마지막 노드를 서로 바꾼다.
# 2) 마지막 노드의 데이터를 변수에 저장한다.
# 3) 마지막 노드를 삭제한다.
# 4) start 노드에 heapify를 호출해서 망가진 힙 속성을 고친다.
# 변수에 저장한 데이터를 리턴한다.(최고 우선 순위 데이터)

def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 메소드"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산

    if (parent_index != 0) and (tree[index] > tree[parent_index]):
        swap(tree, index, parent_index)
        reverse_heapify(tree, parent_index)

class PriorityQueue:
    """힙으로 구현한 우선순위 큐 클래스"""
    def __init__(self):
        self.heap_test_1 = [None]  # 파이썬 리스트로 구현한 힙

    def __str__(self):
        return str(self.heap_test_1)

    def insert(self, data):
        """삽입 메소드"""  # 시간 복잡도 : O(log(n))
        self.heap_test_1.append(data)  # 맨 마지막 인덱스에 데이터 추가

        reverse_heapify(self.heap_test_1, len(self.heap_test_1) - 1)  # 맨 마지막에 추가된 데이터에 대해 reverse_heapify 실행

    def extract_max(self):
        """최고 우선 순위 데이터 추출 메소드"""  # 시간 복잡도 : O(log(n))
        swap(self.heap_test_1, 1, -1)  #
        return_value = self.heap_test_1.pop()
        heapify(self.heap_test_1, 1, len(self.heap_test_1))

        return return_value


# test_code
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)
print(priority_queue)

print(priority_queue.extract_max())
print(priority_queue)


# 여러가지 자료구조로 힙 구현 시 시간 복잡도
# 정렬된 동적배열 - 데이터 삽입 : O(n), 데이터 추출 : O(1)
# 정렬된 이중 연결 리스트 - 데이터 삽입 : O(n), 데이터 추출 : O(1)
# 힙 - 데이터 삽입 : O(log(n)), 데이터 추출 : O(log(n))


## 이진 탐색 트리(Binary Serach Tree)
# 딕셔너리, 세트 등의 추상 자료형 구현 가능

class Node:
    """이진 탐색 트리 노드"""
    def __init__(self, data):
        self.data = data
        self.parent = None  # 부모에 대한 레퍼런스
        self.left_child = None
        self.right_child = None

def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data, end = " ")
        print_inorder(node.right_child)

class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.start = None

    def insert(self, data):
        """이진 탐색 트리 삽입 메소드. 해당 데이터를 가지고 있는 노드로 접근하여 그 노드를 리턴한다."""
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 start 노드로 만든다
        if self.start is None:
            self.start = new_node
            return

        cur_node = self.start  # 삽입될 노드와 비교 대상이 될 노드

        while True:
            if cur_node.data <= new_node.data:  # 현재 노드의 데이터가, 삽입될 노드의 데이터보다 크거나 같은 경우
                if cur_node.right_child is None:  # 오른쪽 노드가 비어 있는 경우
                    cur_node.right_child = new_node  # 현재 노드의 오른쪽 자식 노드로 삽입
                    new_node.parent = cur_node  # new_node의 부모 노드로 이전 노드 설정
                    break
                cur_node = cur_node.right_child  # 오른쪽 노드가 비어 있지 않은 경우
            else:  # 현재 노드의 데이터가, 삽입될 노드의 데이터보다 작은 경우
                if cur_node.left_child is None:  # 왼쪽 노드가 비어 있는 경우
                    cur_node.left_child = new_node  # 현재 노드의 왼쪽 자식 노드로 삽입
                    new_node.parent = cur_node  # new_node의 부모 노드로 이전 노드 설정
                    break
                cur_node = cur_node.left_child  # 왼쪽 노드가 비어 있지 않은 경우

    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        current_node = self.start

        while True:
            if current_node is None:  # 현재 노드가 비어 있는 경우
                return None  # None을 리턴
            elif current_node.data < data:  # 현재 노드의 데이터가, 찾는 데이터보다 작은 경우
                current_node = current_node.right_child  # 오른쪽 자식 노드로 이동
            elif current_node.data > data:  # 현재 노드의 데이터가, 찾는 데이터보다 큰 경우
                current_node = current_node.left_child  # 왼쪽 자식 노드로 이동
            else:  # 현재 노드의 데이터와 찾는 데이터가 일치하는 경우
                return current_node

    def delete(self,data):
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다.
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 경우 1) 삭제하려는 노드가 leaf 노드인 경우
        if (node_to_delete.left_child is None) and (node_to_delete.right_child is None):
            if node_to_delete is self.start:  # 삭제하려는 노드가 루트 노드인 경우
                self.start = None
            else:
                if node_to_delete is parent_node.left_child:  # 삭제하려는 노드가 왼쪽 자식 노드인 경우
                    parent_node.left_child = None
                else:  # 삭제하려는 노드가 오른쪽 자식 노드인 경우
                    parent_node.right_child = None

        # 경우 2) 삭제하려는 노드의 자식이 하나인 노드일 경우
        elif node_to_delete.left_child is None:  # 삭제하려는 노드의 오른쪽 자식 노드만 있는 경우
            if node_to_delete is self.start:  # 루트 노드를 삭제하려는 경우
                self.start = node_to_delete.right_child
                self.start.parent = None
            elif node_to_delete is parent_node.left_child:  # 삭제하려는 노드가 부모 노드의 왼쪽 자식 노드인 경우
                parent_node.left_child = node_to_delete.right_child  # 부모 노드의 왼쪽 자식 노드로, 삭제하려는 노드의 오른쪽 자식 노드 연결
                node_to_delete.right_child.parent = parent_node  # 삭제하려는 노드의 오른쪽 자식 노드의 부모 노드로, 삭제하려는 노드의 부모 노드 연결
            else:  # 삭제하려는 노드가 부모 노드의 오른쪽 자식 노드인 경우
                parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node

        elif node_to_delete.right_child is None:  # 삭제하려는 노드의 왼쪽 자식 노드만 있는 경우
            if node_to_delete is self.start:  # 루트 노드를 삭제하려는 경우
                self.start = node_to_delete.left_child
                self.start.parent = None
            elif node_to_delete is parent_node.left_child:  # 삭제하려는 노드가 부모 노드의 왼쪽 자식 노드인 경우
                parent_node.left_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
            else:  # 삭제하려는 노드가 부모 노드의 오른쪽 자식 노드인 경우
                parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node

        # 경우 3) 삭제하려는 노드의 자식이 2개인 노드일 경우
        elif node_to_delete.left_child and node_to_delete.right_child:
            successor = self.find_min(node_to_delete.right_child)  # successor 노드 : 삭제하려는 노드의 오른쪽 자식 노드의 부분 트리 중, 최솟값을 갖는 노드
            node_to_delete.data = successor.data  # successor 노드의 데이터를 삭제하려는 노드의 데이터에 넣는다.

            if successor is successor.parent.left_child:  # successor 노드가 부모 노드의 왼쪽 자식인 경우
                successor.parent.left_child = successor.right_child  # successor 노드의 부모 노드의 왼쪽 자식으로, successor 노드의 오른쪽 자식 노드(없으면 None) 연결
            else:  # successor 노드가 부모 노드의 오른쪽 자식인 경우
                successor.parent.right_child = successor.right_child

            if successor.right_child is not None:  # successor 노드의 오른쪽 자식 노드가 있는 경우
                successor.right_child.parent = successor.parent  # 해당 노드의 부모 노드로, successor 노드의 부모 노드 연결


    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.start)  # start 노드를 in-order로 출력한다
        print()

    @staticmethod
    def find_min(node):
        """해당 노드를 루트 노드로 갖는 (부분) 이진 탐색 트리의 가장 작은 노드를 리턴"""
        current_node = node

        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node


# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
bst.print_sorted_tree()

# 이진 탐색 트리 탐색 및 노드 출력
print(bst.search(9))

# 부분 이진 탐색 트리의 가장 작은 노드 출력
print(bst.find_min(bst.start).data)

# 이진 탐색 트리 노드 삭제
bst.delete(7)
bst.delete(11)
bst.delete(19)
bst.print_sorted_tree()

# 이진 탐색 트리 연산 (h : 트리의 높이)
# 삽입, 탐색, 삭제 : O(h) (평균적으로 O(log(n)), 최악의 경우 O(n))
# 이진 탐색 트리는 데이터 사이에 순서를 저장해주는 자료구조이므로, 해시 테이블로 구현할 수 없는 정렬 기능을 구현할 수 있다.
# 딕셔너리의 key를 정렬된 상태로 사용하고 싶을 때 이진 탐색 트리를 사용한다.(연산의 효율성은 떨어짐)
'''


## 그래프
# 연결 데이터를 저장할 수 있는 자료구조

# 노드(정점, Vertex) : 그래프에서 하나의 데이터 단위를 나타내는 객체
# 엣지(Edge) : 그래프에서 두 노드의 직접적인 연결 관계 데이터 / 두 노드 사이에 엣지가 있을 때, 두 노드는 "인접해 있다"라고 표현한다.
    # 유향 그래프(dirceted graph) : 방향 그래프에서는 엣지들이 방향을 갖는다. -> 일방적인 관계를 나타낼 수 있다.
    # 가중치 그래프(weighted graph) : 엣지들이 어떤 정보를 나타내는 수치를 갖는다.
# 차수 : 하나의 노드에 연결된 엣지들의 수
    # 무향 그래프에서는 하나의 노드에 연결된 엣지들의 수를 나타낸다.
    # 유향 그래프에서는 노드를 떠나는 엣지의 수를 출력 차수, 노드에 들어오는 엣지의 수를 입력 차수로 구별해서 부른다.
# 경로 : 한 노드에서 다른 노드까지 가는 길
    # 경로의 거리
        # 비가중치 그래프 : 한 경로에 있는 엣지의 수
        # 가중치 그래프 : 한 경로에 있는 엣지의 가중치의 합
    # 최단 경로 : 두 노드 사이의 경로 중 거리가 가장 짧은 경로
# 사이클 : 한 노드에서 시작해서 같은 노드로 돌아오는 경로

# 엣지의 구현
# 1. 인접 행렬

# 모든 요소를 0으로 초기화시킨 크기 6 x 6 인접 행렬
import heapq

adjacency_matrix = [[0 for i in range(6)] for i in range(6)]
adjacency_matrix[0] = [0,1,1,0,0,0]
adjacency_matrix[1] = [1,0,0,1,0,1]
adjacency_matrix[2] = [1,0,0,0,0,1]
adjacency_matrix[3] = [0,1,0,0,1,1]
adjacency_matrix[4] = [0,0,0,1,0,1]
adjacency_matrix[5] = [0,1,1,1,1,0]

print(adjacency_matrix)

# 2. 인접 리스트
# 각 노드의 엣지를 리스트에 저장하는 방법
# 노드의 개수가 n개인 그래프라면, n개의 연결 리스트로 구성 (연결리스트가 없는 경우, 즉 차수가 0인 경우 포인터 변수의 값은 null이 된다.)

# 무향 그래프
graph = {'A': set(['B', 'C']),
	'B': set(['A', 'D']),
        'C': set(['A', 'E', 'F']),
        'D': set(['B', 'E', 'G']),
        'E': set(['C', 'D', 'H']),
        'F': set(['C']),
        'G': set(['D']),
        'H': set(['E'])}


#인접 행렬과 인접 리스트 비교

# V (Vertex) : 그래프 안에 있는 모든 노드들의 집합 (모든 노드의 수)
# E (Edge) : 그래프 안에 있는 모든 엣지들의 집합 (모든 엣지의 수)

# 노드 수가 V 일 때, 무방향 그래프는 V^2/2, 방향 그래프는 V^2개의 엣지를 갖는다.
# 인접 행렬 공간 복잡도 : O(V^2)
# 인접 리스트 공간 복잡도 : O(V + E) (인접 리스트 자체를 저장하는데 O(V), 엣지 저장 하는데 O(E)) (최악의 경우 O(V^2))


# 그래프 탐색
# 하나의 시작점 노드에서 연결된 노드들을 모두 찾는 것


## BFS(Breadth First Search) (너비 우선 탐색)
# 그래프를 너비 우선적으로 탐색

# 시작 노드를 방문 후, 큐에 넣는다.
# 큐에 아무 노드가 없을 때까지
    # 큐 가장 앞 노드를 꺼낸다
    # 꺼낸 노드에 인접한 노드들을 모두 보면서
        # 처음 방문한 노드면
            # 방문한 노드 표시를 해준다
            # 큐에 넣어준다.

from collections import deque

graph_list = {'A': set(['B', 'C']),
	'B': set(['A', 'D']),
        'C': set(['A', 'E', 'F']),
        'D': set(['B', 'E', 'G']),
        'E': set(['C', 'D', 'H']),
        'F': set(['C']),
        'G': set(['D']),
        'H': set(['E'])}
root_node = 'A'


def BFS_with_adj_list(graph, start):
    """인접 리스트와 큐를 이용한 BFS 탐색 메소드"""
    visited = []  # 방문한 노드가 담길 리스트
    queue = deque([start])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

print(BFS_with_adj_list(graph_list, root_node))


## DFS(Depth First Search) (깊이 우선 탐색)
# 그래프를 너비 우선적으로 탐색

# 시작 노드를 옅은 회색 표시 후, 스택에 넣는다.
# 스택에 아무 노드가 없을 때까지
    # 스택 가장 위 노드를 꺼낸다
    # 노드를 방문(진한 회색) 표시한다.
    # 인접한 노드들을 모두 보면서
        # 처음 방문하고나 스택에 없는 노드면:
            # 옅은 회색 표실르 해준다.
            # 스택에 넣어준다.

def DFS_with_adj_list(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(DFS_with_adj_list(graph_list, root_node))

# DFS, BFS 시간 복잡도 : O(V + E)


## 최단 경로 알고리즘

# 1. 최단 경로 알고리즘 - BFS

# 시작 노드를 방문 표시 후, 큐에 넣는다.
# 큐에 아무 노드가 없을 때까지
    # 큐 가장 앞 노드를 꺼낸다.
    # 꺼낸 노드에 인접한 노드들을 모두 보면서
        # 처음 방문한 노드면
            # 방문한 노드 표시를 해준다.
            # predecessor 변수를 큐에서 꺼낸 노드로 설정한다.
            # 큐에 넣어준다.

# BackTracking
    # 현재 노드를 경로에 추가한다.
    # 현재 노드의 predecessor로 간다.
    # predecessor가 없을 때까지 위 단계들을 반복한다.

graph_list = {'A': set(['B', 'C']),
	'B': set(['A', 'D']),
        'C': set(['A', 'E', 'F']),
        'D': set(['B', 'E', 'G']),
        'E': set(['C', 'D', 'H']),
        'F': set(['C', 'I']),
        'G': set(['D']),
        'H': set(['E']),
        'I': set(['F'])}
start = 'A'
destination = 'I'


def BFS_shortest_path(graph, start, destination):
    """인접 리스트와 큐를 이용한 BFS 최단경로 탐색 메소드"""
    visited = []  # 방문한 노드가 담길 리스트
    queue = deque([start])

    predecessor_list = {}  # predecssor가 담길 리스트
    for key in graph_list.keys():
        predecessor_list[key] = None

    while queue:
        n = queue.popleft()  # BFS 알고리즘과 동일
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)

            for i in graph[n]:  # n에 인접한 노드들을 돌면서
                if (predecessor_list[i] is None) and (i is not start):  # predecessor가 설정되어 있지 않고, 루트 노드가 아닌 경우
                    predecessor_list[i] = n  # predecessor 설정

    # Back Tracking
    current_node = destination  # 탐색을 시작한 현재 노드로, destination 설정
    res_str = current_node  # 경로가 추가될 문자열
    while predecessor_list[current_node] is not None:
        res_str = f"{predecessor_list[current_node]}->{res_str}"
        current_node = predecessor_list[current_node]

    return f'The shortest path from "{start}" to" {destination}" in this graph  : "{res_str}"'

print(BFS_shortest_path(graph_list, start, destination))


# 2. 최단 경로 알고리즘 - 다익스트라(Dijkstra)

# 파이썬 heapq 모듈
# 파이썬의 일반 리스트를 마치 최소 힙처럼 다룰 수 있게 해준다.
import heapq

heap_test_1 = []

# 힙에 원소 추가
heapq.heappush(heap_test_1, 4)
heapq.heappush(heap_test_1, 1)
heapq.heappush(heap_test_1, 7)
heapq.heappush(heap_test_1, 3)
heapq.heappush(heap_test_1, 5)
print(heap_test_1)

# 힙에서 원소 삭제
print(heapq.heappop(heap_test_1))
print(heap_test_1)

heap_test_2 = [4,13,17,6,2,1,5]
heapq.heapify(heap_test_2)
print(heap_test_2)


# 응용 1) 최대 힙
nums = [4, 1, 7, 3, 8, 5]
heap = []
max_heap = []
for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  max_heap.append(heapq.heappop(heap)[1])

print(max_heap)


# 응용 2) K번째 최소값/최대값
def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))


# 응용 3) 힙 정렬
def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))


# 다익스트라 알고리즘 구현

import heapq
import sys

def dijkstra(start):
    distances = {node : sys.maxsize for node in graph}  # 초기 배열 설정
    distances[start] = 0  # 시작 노드 distance는 0으로 설정
    queue = []

    heapq.heappush(queue, (distances[startp], start))  # (거리, 노드) -> heapq 모듈에서 첫 번째 데이터를 기준으로 정렬하기 때문

    while queue:  # 우선 순위 큐에 데이터가 없을 때까지
        current_dist, node = heapq.heappop(queue)  # 가장 낮은 거리를 가진 노드와 거리 추출

        if distances[node] < current_dist:  # (거리, 노드)의 형태로 저장되어, 동일한 노드도 큐에 저장되는데, 이를 해결하기 위함
            continue

        for adj_node, dist in graph[node].items():  # 대상인 노드에서 인접한 노드와 거리를 순회
            weighted_dist = current_dist + dist  # 현재 노드에서 인접한 노드를 지나갈 때까지의 거리를 더함
            if weighted_dist < distances[adj_node]:  # 배열의 저장된 거리보다 위의 가중치가 더 작으면 해당 노드의 거리 변경
                distances[adj_node] = weighted_dist

                heapq.heappush(queue, (weighted_dist, adj_node))

    return distances

graph = {
    'A' : {'B':10, 'C':3},
    'B' : {'C':1, 'D':2},
    'C' : {'B':4, 'D':8, 'E':2},
    'D' : {'E':7},
    'E' : {'D':9}
}

result = dijkstra('A')
print(result)