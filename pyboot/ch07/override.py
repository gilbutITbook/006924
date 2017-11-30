class A:
    def hello(self): #Class A의 hello함수
        print('Class A says Hello')

class B(A):
    def hello(self): #Class B의 hello 함수
        print('Class B says Hello')

b = B() #Class B 객체 생성
b.hello() #객체를 사용해서 hello 함수 호출
