class Human:
    age = 0 #연령
    lastname = '' #성
    firstname = ''  #이름
    height = 0.0
    weight = 0.0

a = Human()
a.age = 30
a.lastname = '김'
a.firstname = '철수'
a.height = 180.5
a.weight = 70.2

print(a.age)
print(a.lastname + " " + a.firstname)
