class Human:
    age = 0
    lastname = ''
    firstname = ''
    height = 0.0
    weight = 0.0

younghee = Human()
younghee.age = 35
younghee.lastname = '이'
younghee.firstname = '영희'
younghee.height = 174.1
younghee.weight = 68.2

if( younghee.age >= 35 and younghee.firstname == '영희'):
    print('선택된 사람->' + younghee.lastname + ' ' + younghee.firstname)
