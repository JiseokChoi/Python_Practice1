
### 객체 지향 프로그래밍
# 필요한 데이터를 추상화시켜, 속성과 행동를 가진 객체를 만들고, 그 객체들 간의 유기적인 상호작용을 통해 로직을 구성하는 프로그래밍 방법
# 속성 : 변수 / 행동 : 메소드(함수)


# 인스턴스 메소드 : 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
# 인스턴스 메소드의 첫 번째 파라미터는 'self'로 사용하자!

class User:
    # 인사 메시지 출력 메소드
    def say_hello(self):
        print(f"안녕하세요. {self.name}입니다!")

# 인스턴스(객체) 생성
user1 = User()
user1.name = "Jones"
user1.email = "hello123@gmail.com"

User.say_hello(user1)
# 인스턴스의 메소드로 호출 시, user1 인스턴스가 say_hello의 첫 번째 파라미터로 자동 전달
user1.say_hello()


# __init__ 메소드(초기화 메소드)
# 인스턴스 생성 시, __init__메소드 자동 호출

# __str__메소드(문자열 반환 메소드)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'사용자 이름 : {self.name}, 사용자 이메일 : {self.email}'

    def say_hello(self):
        print(f"안녕하세요. {self.name}입니다!")

user1 = User("Jones", "hello123@gmail.com")
user1.say_hello()
print(user1)  # 사용자 이름 : Jones, 사용자 이메일 : hello123@gmail.com


# 클래스 변수
class User:
    count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.count += 1  # 클래스 변수 (접근은 클래스명.클래스 변수)

user1 = User("Jones", "hello123@gmail.com")
user2 = User("Tim", "hi456@naver.com")

print(User.count)  # 2
print(user1.count)  # 2
print(user2.count)  # 2


# 데코레이터(Decorator)_1
# 어떤 함수를 받아, 부가 기능을 덧붙여 리턴(꾸며주는 기능)

def print_hello():
    print("안녕하세요!")

def add_print_to(original):
    def wrapper():
        print("함수 시작")  # 부가 기능1
        original()
        print("함수 끝")  # 부가 기능2
    return wrapper

print_hello = add_print_to(print_hello)
print_hello()


# 데코레이터(Decorator)_2
def add_print_to(original):
    def wrapper():
        print("함수 시작")  # 부가 기능1
        original()
        print("함수 끝")  # 부가 기능2
    return wrapper

@add_print_to  # 데코레이터 (@classmethod)
def print_hello():
    print("안녕하세요!")

print_hello()


# 클래스 메소드1

class User:
    count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.count += 1

    def __str__(self):
        return f'사용자 이름 : {self.name}, 사용자 이메일 : {self.email}'

    def say_hello(self):
        print(f"안녕하세요. {self.name}입니다!")

    @classmethod  # 클래스 메소드는 첫 번째 파라미터(cls)로 class가 자동 전달
    def number_of_users(cls):
        print(f'총 유저 수는 : {cls.count}입니다.')

    # 정적 메소드(Static method) : 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드 -> 인스턴스, 클래스에서 모두 호출 가능
    @staticmethod
    def is_valid_email(email_address):
        return "@" in email_address

user1 = User("Jones", "hello123@gmail.com")
print(user1.is_valid_email("hello123@gmail.com"))
User.number_of_users()
user1.number_of_users()



# 클래스 메소드와 인스턴스 메소드 비교
# 1. 인스턴스 메소드 사용 : User.say_hello(user1), user1.say_hello() / 인스턴스 자신이 첫 번째 파라미터로 자동 전달
# 2. 클래스 메소드 사용 : User.number_of_users(), user1.number_of_users() / 첫 번째 파라미터로 클래스가 자동 전달

# 인스턴스 변수를 사용하지 않는 경우(클래스 변수만 사용) -> 클래스 메소드를 사용한다.

# 절차 지향 프로그래밍과 객체 지향 프로그래밍의 차이
# 1. 절차 지향 프로그래밍 : 프로그램을 만들 때, 데이터와 함수를 합칠 수 없음. 프로그램을 명령어들을 순서대로 실행하는 것으로 봄.
# 2. 객체 지향 프로그래밍 : 프로그램을 만들 때, 데이터와 함수를 합칠 수 있음. 프로그램을 객체들이 순서대로 상호작용하는 것으로 봄.


### 객체 지향 프로그래밍의 4가지 특징

## 1. 추상화(Abstraction)
# 복잡한 자료, 모듈, 시스템 등으로부터 사용에 꼭 필요한 핵심적인 개념 또는 기능을 간추려 내는 것(세부사항은 가림)
# 예를 들어, list 클래스의 코드 전체를 알지 못하더라도, 리스트를 사용할 수 있음. -> 추상화 덕분
# 추상화 팁 : 1) 클래스, 변수, 메소드 이름을 직관적으로 정의. 2) 문서화(docstring)

# 파이썬 타입 힌트(Type hinting) : "변수명: 타입" / 함수 -> 반환값 타입
# 코드에 직접적인 영향은 주지 않음. 파이썬 3.5ver 이상부터 사용 가능

class BankAccount():
    """은행 계좌 클래스"""
    interest = 0.02

    def __init__(self, owner_name: str, balance: float) -> None:
        """인스턴스 변수 : name(문자열), balance(실수형)"""
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """잔액 인스턴스 변수 balance를 파라미터 amount 만큼 늘려주는 메소드"""
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """잔액 인스턴스 변수 balance를 파라미터 amount 만큼 줄여주는 메소드"""
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def add_interest(self) -> None:
        """잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드"""
        self.balance *= 1 + BankAccount.interest

help(BankAccount)  # 클래스에 대한 설명(메소드 이름, docstring)


# 문서화(docstring) 스타일

# 1) Google docstring
"""유저에게 추천할 영상을 찾아준다
Parameters:
  number_of_suggestions (int): 추천하고 싶은 영상 수
    (기본값은 5)

Returns:
  list: 추천할 영상 주소가 담긴 리스트
"""

# 2) reStructured_text(Python official documentation standard)
"""유저에게 추천할 영상을 찾아준다

:param number_of_suggestions: 추천하고 싶은 영상 수
  (기본값은 5)
:type number_of_suggestions: int
:returns: 추천할 영상 주소가 담긴 리스트
:rtype: list
"""

# 3) Numpy/SciPy
"""유저에게 추천할 영상을 찾아준다

Parameters
----------
number_of_suggestions: int
  추천하고 싶은 영상 수 (기본값은 5)

Returns
-------
list 
  추천할 영상 주소가 담긴 리스트
"""


## 2. 캡슐화(Encapsulation)
# 1) 객체의 일부 구현 내용에 대한 외부로부터의 '직접적인' 액세스를 차단하는 것
# 2) 객체의 속성과, 그것을 사용하는 행동을 하나로 묶는 것(변수 접근을 메소드로 제한)

class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.set_age(age)
        self.__resident_id = resident_id

    def authenticate(self, id, field):
        """본인이 맞는지 확인하는 메소드"""
        return self.resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는" + str(self.age) + "살입니다."

    def get_age(self):
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드 (getter)"""
        return self.__age

    def set_age(self, value):
        """숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드 (setter)"""
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정했습니다.")
            self.__age = 0
        else:
            self.__age = value


Jones = Citizen("Jones", 20, "123456-7891011")
# 변수나 메소드 앞에 "__(언더바 2개)"를 붙이면, 클래스 외부에서 사용 불가
# print(Jones.__resident_id) -> AttributeError: 'Citizen' object has no attribute '__resident_id'
print(Jones.get_age())
# 사실 변수나 메소드 앞에 "__"를 사용하면 그 앞에 추가적으로 "_클래스명"을 덧붙여서 이름을 바꿔버리는 것 뿐임(name mangling)
print(Jones._Citizen__resident_id)

# 파이썬에서는 캡슐화를 지원하지 않음(Java 같은 경우 private으로 캡슐화)
# 대신 "_변수명", "_함수명"으로 정의하여, 클래스 외부에서 직접 접근하여 사용하지 말라고 약속함(강제력 X)


# 데코레이터 함수(Property)를 사용한 캡슐화
class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self._age = age
        self._resident_id = resident_id

    def authenticate(self, id, field):
        """본인이 맞는지 확인하는 메소드"""
        return self.resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는" + str(self.age) + "살입니다."

    @property
    def age(self):
        """getter 메소드"""
        print("나이를 리턴합니다.")
        return self._age

    @age.setter
    def age(self, value):
        """setter 메소드"""
        print("나이를 설정합니다.")
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = value

Jones = Citizen("Jones", 20, "123456-7891011")
Jones.age = 21  # setter 함수 실행
print(Jones.age)  # getter 함수 실행 -> 21


## 3. 상속(Inheritance)
#  부모 클래스(Super class)의 속성(property)과 함수(method)를 물려받는 것

class Employee:
    """직원 클래스"""
    company_name = "Laon"  # 가게 이름
    raise_percentage = 1.05  # 시급 인상률

    def __init__(self, name, wage):
        "인스턴스 변수 설정"
        self.name = name  # 이름
        self.wage = wage  # 시급

    def raise_pay(self):
        "시급을 인상하는 메소드"
        self.wage *= self.raise_percentage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원 : " + self.name


class Cashier(Employee):  # Employee 클래스 상속
    """캐셔 클래스"""
    raise_percentage = 1.1
    burger_price = 4000

    # 메소드 오버라이딩(method overriding) : 상속받은 부모 클래스의 메소드를 재정의하여 사용하는 것
    # mro에 의해 메소드 실행 순서 결정(메소드 검색 방향 : 자식 -> 부모)
    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)  # super() 메소드 : 자식 클래스에서 상속받은 부모 클래스의 내용을 사용하고 싶을 때
        self.number_sold = number_sold

    def __str__(self):
        return Cashier.company_name + " 계산대 직원 : " + self.name
    
    # 부모 클래스에 없는 기능(메서드) 추가
    def take_order(self, money_received):
        """주문과 돈을 받고 거스름돈을 리턴한다"""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다. 돈을 다시 계산해서 주세요.")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

Jones = Cashier("Jones", 5000, 4)
Jones.raise_pay()
print(Jones.wage)
print(Jones)

help(Cashier)

# mro 메소드(Method resolution order) : 자식과 부모 클래스를 전부 포함하여, 메소드 결정 순서를 지정하는 것(죽음의 다이아몬드 문제 해결)
# 나온 순서대로 우선 순위가 높음

print(Cashier.mro())  # [<class '__main__.Cashier'>, <class '__main__.Employee'>, <class 'object'>]
print(IndentationError.mro())  # [<class 'IndentationError'>, <class 'SyntaxError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]


# 파이썬 다중상속 : 여러 부모 클래스를 상속받는 것

class Programmer:
    """프로그래머 클래스"""
    def __init__(self, language):
        self.language = language

    def what_lang(self):
        print(f'{self.language} 프로그래밍 언어를 사용합니다.')

class Gamer:
    """게이머 클래스"""
    def __init__(self, game):
        self.game = game

    def what_game(self):
        print(f'{self.game}를(을) 플레이 합니다.')

class MultiTasker(Programmer, Gamer):
    def __init__(self, language, game):
        # super() 사용 시 어느 부모 클래스로부터 상속받을지 결정x (다중상속의 단점) -> Java의 경우 다중상속 지원X
        # super() 실행 시, mro 우선 순위에 따라 실행 (상속 받는 순서에 따라 mro가 바뀜)
        # 다중상속 tip : 1) 부모 클래스끼리 같은 이름의 메소드를 갖지 않도록 하기 2) 같은 이름 메소드는 자식클래스에서 오버라이딩
        Programmer.__init__(self, language)
        Gamer.__init__(self, game)

Jones = MultiTasker("파이썬", "스타크래프트")
Jones.what_lang()
Jones.what_game()


# 4. 다형성(Polymorphism)
# 여러가지 형태를 갖는 성질
# 상속 관계 내의 다른 클래스들의 인스턴스들이 같은 이름의 멤버 함수 호출에 대해 각각 다르게 반응하도록 하는 기능

from math import pi
from abc import ABC, abstractmethod  # Abstract Base Class : 추상 클래스로 만들 수 있음

class Shape(ABC):  #ABC 상속 -> 추상 클래스가 됨(추상 클래스는 인스턴스를 만들 수 없음!)
    """도형 클래스 (이 클래스를 상속받으면, 적어도 하나 이상의 추상 메소드를 오버라이딩 해야 된다)"""
    @abstractmethod
    def area(self) -> float:   # 추상 메소드
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        print("도형의 넓이를 계산한다")

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass  # 내용을 작성하지 않고 넘어감


class Rectangle(Shape):
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Shape 클래스를 상속 받았으므로, Shape 클래스의 메소드를 반드시 오버라이딩 해야 함.
    # 오버라이딩을 강제함
    def area(self):
        """직사각형의 넓이를 리턴한다"""
        super().area()  # 추상 클래스도 부모 클래스이므로, super()로 내용 접근 가능
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        return f"밑변 {self.width}, 높이 {self.height}인 직사각형"


class Circle(Shape):
    """원 클래스"""
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        """원의 넓이를 리턴한다"""
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2 * pi * self.radius
    
    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return f"반지름 {self.radius}인 원"


class Cylinder:
    """실린더 클래스"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        """실린더의 표면적을 리턴한다"""
        return 2 * pi * (radius ** 2) + 2 * pi * radius * height

    def volume(self):
        """실린더의 부피를 리턴한다"""
        return pi * (radius ** 2) * height

    def __str__(self):
        """실린더의 정보를 문자열로 리턴한다."""
        return f"반지름 {self.radius}, 높이 {self.height}인 실린더"


class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):
        """그림판에 도형 인스턴스 shape을 추가한다. 단, shape은 추상 클래스 Shape의 인스턴스여야 한다."""
        self.shapes.append(shape)

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        total_area = 0

        for shape in self.shapes:
            try:  # 일단 해보고 문제가 발생하면 처리 : EAFP 코딩 스타일 (Easier to Ask for Forgiveness than Permission)
                total_area += shape.area()
            except (AttributeError, TypeError):
                print(f"그림판에 area 메소드가 없거나, 잘못 정의되어 있는 인스턴스 {shape}가 있습니다.")

            return total_area

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        total_perimeter = 0

        for shape in self.shapes:
            try:
                total_perimeter += shape.perimeter()
            except (AttributeError, TypeError):
                print(f"그림판에 perimeter 메소드가 없거나, 잘못 정의되어 있는 인스턴스 {shape}가 있습니다.")

        return total_perimeter

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다"""
        res_str = "그림판 안에 있는 도형들 :\n\n "
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str

rectangle = Rectangle(3,7)
circle = Circle(5)
cylinder = Cylinder(4, 6)  # shapes에 추가될 수 없음(Shape 클래스를 상속받지 못했기 때문)

paint_program = Paint()
paint_program.add_shape(rectangle)
paint_program.add_shape(circle)
paint_program.add_shape(cylinder)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())
print(paint_program)


### 견고한 객체지향 프로그래밍을 위한 SOLID 원칙

## 1. 단일 책임 원칙 (Solid responsibility principle)
# 모든 클래스는 단 한 가지의 책임만을 갖고, 클래스 안에 정의되어 있는 모든 기능은 이 하나의 책임을 수행하는데 집중되어야 한다.
# 같이 수정해야될 것들은 묶고, 따로 수정해야될 것들은 분리하는 것

# 단일 책임 원칙을 지키지 않는 경우
class StudentScoreAndCourseManager:
    def __init__(self):
        scores = {}
        courses = {}

    def get_score(self, student_name, course):
        pass

    def get_courses(self, student_name):
        pass

# 단일 책임 원칙을 지키는 경우
# 코드는 길어졌지만, 유지보수가 용이
class ScoreManager:
    def __init__(self):
        scores = {}

    def get_score(self, student_name, course):
        pass


class CourseManager:
    def __init__(self):
        courses = {}

    def get_courses(self, student_name):
        pass


## 2. 개방 폐쇄 원칙 (Open/closed priciple)
# 클래스는 확장에 열려있어야 하며, 수정에는 닫혀 있어야 한다.
# 어떤 코드를 수정하지 않아도, 확장할 수 있어야 한다.
# 개발의 편의성, 코드의 유지보수성 향상상

## 3. 리스코프 치환 원칙(Liskov substitution priciple)
# 부모 클래스의 인스턴스를 사용하는 위치에 자식 클래스의 인스턴스를 대신 사용했을 때 코드가 원래 의도대로 작동해야 한다.
# 부모 클래스의 행동규약을 자식 클래스가 위반하지 말 것
# ㄴ 1) 자식 클래스가 부모 클래스의 변수의 타입을 바꾸거나, 메소드의 파라미터 또는 리턴값의 타입 or 갯수를 바꾸는 경우
# 2) 자식 클래스가 부모 클래스의 의도와 다르게 메소드를 오버라이딩 하는 경우

## 4. 인터페이스 분리 원칙(Interface segregation principle)
# 파이썬에는 없는 개념이지만, 추상 클래스 주에서 추상 메소드만 있고 일반 메소드는 없는 것을 인터페이스라고 한다.
# 클래스가 사용하지 않을 메소드에 의존할 것을 강요하면 안 된다.(클래스가 사용하지도 않을 메소드를 가지도록 강제하면 안 된다는 것)
# 너무 많은 메소드를 한번에 갖고 있는 인터페이스 : 뚱뚱한 인터페이스
# 인터페이스 분리 원칙을 위반하지 않는 방법 -> 인터페이스를 더 작게 쪼갠다.(역할 인터페이스)

## 5. 의존 관계 역전 원칙(Dependency inversion priciple)
# 상위 모듈(하위 모듈을 사용하는 모듈)은 하위 모듈의 구현 내용에 의존하면 안 된다. 상위 모듈과 하위 모듈 모두 추상화된 내용에 의존해야 한다.
# 의존 관계 역전 원칙을 위반하지 않는 방법 -> 의존 관계를 만들지 않는다
# 세부 사항이 추상화에 의존해야 한다.