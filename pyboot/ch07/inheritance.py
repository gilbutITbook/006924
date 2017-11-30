class A:
    name = 'Class A'

class B(A): #Class A를 상속
    pass

b = B()
print(b.name) # Class A 라고 표시된다
