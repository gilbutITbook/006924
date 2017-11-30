class Human:
    age = 0
    lastname = ''
    firstname = ''
    height = 0.0 # 미터 단위
    weight = 0.0 # Kg

    def get_bmi(self):
        return (self.weight) / (self. height ** 2 )

chulsoo = Human()
chulsoo.lastname = '김'
chulsoo.firstname = '철수'
chulsoo.weight = 68
chulsoo.height = 1.7

bmi = chulsoo.get_bmi()
print(bmi)
