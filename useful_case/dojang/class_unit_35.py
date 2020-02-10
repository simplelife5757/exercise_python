b = list(range(10))
c = dict(x=10, y=20)

def factorial(n):
  if not isinstance(n, int) or n < 0:
    return None
  if n == 1:
    return 1
  return n * factorial(n - 1)

# self 없이 메서드 이름만 사용하면 클래스 바깥쪽에 있는 함수 호출 
class Person:
  # __slot__ = ['속성이름1', '속성이름2']
  __slot__ = ['name, age, address']
  
  def __init__(self, name, age, address, wallet):
    self.hello = '안녕하세요'
    self.name = name
    self.age = age
    self.address = address
    # private attribute
    self.__wallet = wallet

  def greeting(self):
    print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

  def pay(self, amount):
    self.__wallet -= amount
    print('이제 {0}원 남았네요.'.format(self.__wallet))

  # private method
  def __greeting(self):
    print('hello')

jiwoo = Person('마리아', 20, '서초구 반포동', 1000)
jiwoo.greeting()

is_instance = isinstance(jiwoo, Person)

# 스페셜 메서드, 매직 메서드 
# 리스트 언패킹 *args
# 딕셔너리 언패킹 **kwargs

def send(recipient, message):
  return (recipient, message)

send(recipient='x', message='y')
