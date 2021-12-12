
# 객체 지향 프로그래밍
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
