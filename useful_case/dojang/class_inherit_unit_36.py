# inheritance
# base class -> derived class

class Person:
  def __init__(self):
    print('Person __init__')
    self.hello = '안녕하세요'
    

class Student(Person):
  def __init__(self):
    print('Student __init__')
    super().__init__()
    self.school = 'school~~~`'

james = Student()
print(james.school)
print(james.hello)
issubclass(Student, Person)

# parent class(base class)의 속성에 접근하기 위해서는 반드시 초기화 해주어야 한다.

# 파생 클래스에서 __init__ 메서드를 생략한다면 기반 클래스의 __init__ 이 자동으로 호출되므로 super()는 사용하지 않아도 된다.

# 오버라이딩은 재정의 

# 파이썬은 다중 상속이 가능 -> 죽음의 다이아몬드 문제 -> 메서드 탐색 순서 (Method Resolution Order, MRO)
# 클래스.mro()

# 추상 클래스 : 메서드의 목록만 가진 클래스, 상속받는 클래스에서 메서드 구현 강제

from abc import *

class StudentBase(metaclass=ABCMeta):
  @abstractmethod
  def study(self):
    pass

  @abstractmethod
  def go_to_school(self):
    pass

class Student(StudentBase):
  def study(self):
    print('공부하기')

  def go_to_school(self):
    print('학교가기')

james = Student()
james.study()
james.go_to_school()