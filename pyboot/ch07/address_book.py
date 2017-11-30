class AddressBook:

    person_list = []

    def add(self, person):
        self.person_list.append(person)

    def show_all(self):
        for person in self.person_list:
            print(person.lastname + " " + person.firstname)

    def search(self,keyword):
        for person in self.person_list:
            if keyword in person.firstname or keyword in person.lastname:
                print(person.lastname + " " + person.firstname)

class Person:
    import datetime

    firstname = ''  # 이름
    lastname = ''  # 성
    tel = ''  # 전화번호
    mail_address = ''  # 메일 주소
    birthday = datetime.datetime(2000, 1, 1)  # 생년월일


ab = AddressBook()

p = Person()
p.firstname = '철수'
p.lastname = '김'
p.tel = '010-1234-5678'

ab.add(p)

p2 = Person()
p2.firstname = 'John'
p2.lastname = 'Lennon'
p2.tel = '010-1234-0098'

print('---동작 확인---')
ab.add(p2)

print('주수록에 등록된 사람 수->' + str(len(ab.person_list)) + ' 명')

print('---목록 표시---')
ab.show_all()

print('--검색--')
ab.search('John')
