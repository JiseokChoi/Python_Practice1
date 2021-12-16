'''
### 파이썬 자료구조

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
'''

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



